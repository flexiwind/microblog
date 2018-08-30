# coding=utf-8

"""
File Name： base_test
Created on: 8/30/18 11:46 AM
Author: feng
Description :

关于大文件的提取和排序问题：

{'PYTHONUNBUFFERED': '1', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'http_proxy': '127.0.0.1:8118', 'XDG_SESSION_DESKTOP': 'ubuntu', 'PIPENV_ACTIVE': '1', 'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0', 'HOME': '/home/feng', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'SHLVL': '2', 'FLASK_APP': 'microblog.py', 'IM_CONFIG_PHASE': '1', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'GOPATH': '/home/feng/nftang/gocode', 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/feng', 'PWD': '/home/feng/nftang/clone_from/microblog/microblog', 'EDITOR': 'vi', 'UPSTART_INSTANCE': '', 'WINDOWID': '69206026', 'GTK2_MODULES': 'overlay-scrollbar', 'COMPIZ_BIN_PATH': '/usr/bin/', 'DESKTOP_SESSION': 'ubuntu', 'VIRTUAL_ENV': '/home/feng/.local/share/virtualenvs/microblog-ui8S106_', 'XAUTHORITY': '/home/feng/.Xauthority', 'XDG_SESSION_TYPE': 'x11', 'QT_ACCESSIBILITY': '1', 'JOB': 'unity-settings-daemon', 'GPG_AGENT_INFO': '/home/feng/.gnupg/S.gpg-agent:0:1', 'GOROOT': '/home/feng/nftang/tools/go', 'INSTANCE': '', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg', 'QT_IM_MODULE': 'fcitx', 'no_proxy': 'localhost,127.0.0.0/8,::1', '_': '/home/feng/.local/share/virtualenvs/microblog-ui8S106_/bin/flask', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'PIP_PYTHON_PATH': '/usr/bin/python', 'DISPLAY': ':0', 'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-pDf8VzpcDJ', 'FLASK_DEBUG': '0', 'QT_LINUX_ACCESSIBILITY_ALWAYS_ON': '1', 'XDG_VTNR': '7', 'QT_QPA_PLATFORMTHEME': 'appmenu-qt5', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'GDM_LANG': 'en_US', 'GTK_IM_MODULE': 'fcitx', 'XDG_CURRENT_DESKTOP': 'Unity', 'CLUTTER_IM_MODULE': 'xim', 'GNOME_KEYRING_PID': '', 'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/2397', 'SESSIONTYPE': 'gnome-session', 'SESSION': 'ubuntu', 'TERM': 'xterm-256color', 'USER': 'feng', 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0', 'NO_PROXY': 'localhost,127.0.0.0/8,::1', 'PS1': '(microblog-ui8S106_) \\[\\e]0;\\u@\\h: \\w\\a\\]${debian_chroot:+($debian_chroot)}\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\W\\[\\033[00m\\]\\$ ', 'XDG_SEAT': 'seat0', 'LANG': 'en_US.UTF-8', 'XDG_SESSION_ID': 'c2', 'SHELL': '/bin/bash', 'LOGNAME': 'feng', 'FLASK_DEBNUG': '1', 'PATH': '/home/feng/.local/share/virtualenvs/microblog-ui8S106_/bin:/home/feng/bin:/home/feng/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/feng/nftang/tools/go/bin', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'https_proxy': '127.0.0.1:8118', 'UPSTART_JOB': 'unity7', 'XDG_RUNTIME_DIR': '/run/user/1000', 'VTE_VERSION': '4205', 'QT4_IM_MODULE': 'fcitx', 'GDMSESSION': 'ubuntu', 'GTK_MODULES': 'gail:atk-bridge:unity-gtk-module', 'COMPIZ_CONFIG_PROFILE': 'ubuntu', 'FLASK_RUN_FROM_CLI': 'true', 'UPSTART_EVENTS': 'xsession started', 'GNOME_KEYRING_CONTROL': '', 'XMODIFIERS': '@im=fcitx', 'LANGUAGE': 'en_US'}
"""
import pprint


def dict_default_method():
    a = [('feng', '111'), ('feng', '121'), ('feng1', '111'), ('feng2', '111'), ('feng2', '121'), ]
    name_count = dict()
    for (name, value) in a:
        name_count.setdefault(name, []).append(value)
    print(name_count)


def bad_append(new_item, a_list=[]):
    a_list.append(new_item)
    return a_list


if __name__ == '__main__':
    print(bad_append(1))
    print(bad_append(2))
    print(bad_append(3))
    print(locals())
    pprint.pprint(locals())

{'PYTHONUNBUFFERED': '1',
 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path',
 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop',
 'http_proxy': '127.0.0.1:8118',
 'XDG_SESSION_DESKTOP': 'ubuntu',
 'PIPENV_ACTIVE': '1',
 'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0',
 'HOME': '/home/feng',
 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path',
 'SHLVL': '2',
 'FLASK_APP': 'microblog.py',
 'IM_CONFIG_PHASE': '1',
 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh',
 'GOPATH': '/home/feng/nftang/gocode',
 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/feng',
 'PWD': '/home/feng/nftang/clone_from/microblog/microblog',
 'EDITOR': 'vi',
 'UPSTART_INSTANCE': '',
 'WINDOWID': '69206026',
 'GTK2_MODULES': 'overlay-scrollbar',
 'COMPIZ_BIN_PATH': '/usr/bin/',
 'DESKTOP_SESSION': 'ubuntu',
 'VIRTUAL_ENV': '/home/feng/.local/share/virtualenvs/microblog-ui8S106_',
 'XAUTHORITY': '/home/feng/.Xauthority',
 'XDG_SESSION_TYPE': 'x11', 'QT_ACCESSIBILITY': '1', 'JOB': 'unity-settings-daemon',
 'GPG_AGENT_INFO': '/home/feng/.gnupg/S.gpg-agent:0:1', 'GOROOT': '/home/feng/nftang/tools/go', 'INSTANCE': '',
 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:',
 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg', 'QT_IM_MODULE': 'fcitx',
 'no_proxy': 'localhost,127.0.0.0/8,::1', '_': '/home/feng/.local/share/virtualenvs/microblog-ui8S106_/bin/flask',
 'LESSOPEN': '| /usr/bin/lesspipe %s', 'PIP_PYTHON_PATH': '/usr/bin/python', 'DISPLAY': ':0',
 'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-pDf8VzpcDJ', 'FLASK_DEBUG': '0',
 'QT_LINUX_ACCESSIBILITY_ALWAYS_ON': '1', 'XDG_VTNR': '7', 'QT_QPA_PLATFORMTHEME': 'appmenu-qt5',
 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'GDM_LANG': 'en_US', 'GTK_IM_MODULE': 'fcitx', 'XDG_CURRENT_DESKTOP': 'Unity',
 'CLUTTER_IM_MODULE': 'xim', 'GNOME_KEYRING_PID': '',
 'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/2397', 'SESSIONTYPE': 'gnome-session',
 'SESSION': 'ubuntu', 'TERM': 'xterm-256color', 'USER': 'feng',
 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0', 'NO_PROXY': 'localhost,127.0.0.0/8,::1',
 'PS1': '(microblog-ui8S106_) \\[\\e]0;\\u@\\h: \\w\\a\\]${debian_chroot:+($debian_chroot)}\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\W\\[\\033[00m\\]\\$ ',
 'XDG_SEAT': 'seat0', 'LANG': 'en_US.UTF-8', 'XDG_SESSION_ID': 'c2', 'SHELL': '/bin/bash', 'LOGNAME': 'feng',
 'FLASK_DEBNUG': '1',
 'PATH': '/home/feng/.local/share/virtualenvs/microblog-ui8S106_/bin:/home/feng/bin:/home/feng/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/feng/nftang/tools/go/bin',
 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'https_proxy': '127.0.0.1:8118', 'UPSTART_JOB': 'unity7',
 'XDG_RUNTIME_DIR': '/run/user/1000', 'VTE_VERSION': '4205', 'QT4_IM_MODULE': 'fcitx', 'GDMSESSION': 'ubuntu',
 'GTK_MODULES': 'gail:atk-bridge:unity-gtk-module', 'COMPIZ_CONFIG_PROFILE': 'ubuntu', 'FLASK_RUN_FROM_CLI': 'true',
 'UPSTART_EVENTS': 'xsession started', 'GNOME_KEYRING_CONTROL': '', 'XMODIFIERS': '@im=fcitx', 'LANGUAGE': 'en_US'}
