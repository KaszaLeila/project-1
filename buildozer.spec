[app]
package.name = myspeechemotionapp
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas,wav,model,result

# (str) Application versioning (method1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pyaudio,numpy,librosa,scikit-learn,soundfile

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = RECORD_AUDIO,WRITE_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 27

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (int) Android NDK version to use
android.ndk = 19b

# (bool) Use --private data storage
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.renpy.android.PythonActivity

# (list) Application meta-data
#android.meta_data = key=value

# (list) buildozer action to be used (list of str)
#action_modes = list-append
