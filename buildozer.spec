[app]

# Title of your application
title = Speech Emotion Recognition

# Package name
package.name = speechemotionrecognition

# Package domain
package.domain = org.test

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1

# Kivy version
osx.kivy_version = 2.1.0

# Application requirements
requirements = python3==3.7.6,hostpython3==3.7.6,kivy,pyaudio,soundfile,numpy,librosa,scikit-learn,pillow

# Supported orientations
orientation = portrait

# Android specific settings
fullscreen = 0
android.arch = armeabi-v7a
android.ndk = 25b
android.api = 31
android.minapi = 21

# Permissions
android.permissions = RECORD_AUDIO,WRITE_EXTERNAL_STORAGE

# Python for android (p4a) settings
p4a.branch = master
p4a.source_dir =
p4a.local_recipes =

[buildozer]

# Log level
log_level = 2

# Display warning if run as root
warn_on_root = 1
