from django.db import models
from django.conf import settings
import subprocess
import os

class Video(models.Model):
    """動画"""

    title = models.CharField('動画タイトル', max_length=255)
    description = models.TextField('説明(空欄可)', blank=True)
    thumbnail = models.ImageField('サムネイル(空欄可)', upload_to='thumbnails/', null=True, blank=True)  # /media/thumbnails/ファイル名
    upload = models.FileField('ファイル', upload_to='uploads/%Y/%m/%d/')  # /media/uploads/2018/3/20/ファイル名
    hls_path = models.FileField('HLSファイル', blank=True, null=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)  # default=timezone.nowと違い、入力欄は表示されない
    updated_at = models.DateTimeField('更新日', auto_now=True)  # 更新するたびにその日時が格納される

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.hls_path:
            self.convert_to_hls()

    def convert_to_hls(self):
        # アップロードされたファイルのパスを取得
        input_file = self.upload.path
        
        # 出力先ディレクトリをアップロードされたファイルと同じにする
        output_dir = os.path.dirname(input_file)
        output_file_base = os.path.splitext(os.path.basename(input_file))[0]
        hls_output_path = os.path.join(output_dir, f"{output_file_base}_hls")
        
        # 出力ディレクトリが存在しない場合は作成
        os.makedirs(hls_output_path, exist_ok=True)

        # ffmpegを使用して動画をHLS形式に変換
        command = [
            'ffmpeg', '-i', input_file,
            '-s', '640x360',
            '-hls_time', '1', '-hls_list_size', '0',
            '-f', 'hls', os.path.join(hls_output_path, 'index.m3u8')
        ]
        subprocess.run(command, check=True)
        
        # HLSパスを更新
        self.hls_path = os.path.join(hls_output_path, 'index.m3u8').lstrip(settings.MEDIA_ROOT)
        super().save(update_fields=['hls_path'])