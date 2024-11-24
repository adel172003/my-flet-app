[app]
title = My Ad App
package.name = adapp
package.domain = org.test
source.dir = .
source.include_exts = py
version = 0.1

requirements = python3,flet,kivy

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1