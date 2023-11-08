import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import sys

# 读取音频wav文件
audio_path = r"D:\piano.wav"
y, sr = librosa.load(audio_path, sr=None, mono=True)
"""
:param
    path	音频路径
    sr	采样率（默认22050，但是有重采样的功能）
    mono	设置为true是单通道，否则是双通道
    offset	音频读取的时间
    duration	什么玩意儿

:returns
    y : 音频的信号值，类型是ndarray
    sr : 采样率
"""
###############################################################################

###############################################################################
# plt画图
f, ((ax11, ax12)) = plt.subplots(1, 2, sharex=False, sharey=False)
###################################################################
# 01 左，信号
ax11.set_title('Signal')
ax11.set_xlabel('Time (samples)')
ax11.set_ylabel('Amplitude')
ax11.plot(y)
###################################################################
# 02 右，傅里叶变换
n_fft = 2048
ft = np.abs(librosa.stft(y[:n_fft], hop_length=n_fft+1))
ax12.set_title('Spectrum')
ax12.set_xlabel('Frequency Bin')
# ax12.set_ylabel('Amplitude')
ax12.plot(ft)
################################################################################

plt.show()
