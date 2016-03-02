Name: icex-startup
Version: 0.16
Release: alt8

Summary: simple pluggable IceWM autostart manager

Summary(ru_RU.UTF-8): менеджер автозапуска программ IceWM
License: GPL
Group: Graphical desktop/Icewm
Url: http://git.altlinux.org

Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Source0: icewm.tar
Source1: XXkb.conf

BuildArch: noarch
AutoReq: no

# uncomment if you want to backport prior to M30
#define icewmconfdir #_x11x11dir/icewm
#%define icewmconfdir %_sysconfdir/icewm
%define icewmconfdir %_datadir/icewm
#due to new icewmconfdir in /etc/X11
#Requires: icewm >= 1.3.11
##Requires: icewm-x-githubmod

Conflicts: icewm-startup icewm-x-startup

%description
Simple pluggable icewm autostart manager is a generic IceWM startup script
which allows one to configure IceWM default autostart via installing corresponding rpm plug-ins.

%description -l ru_RU.UTF-8
менеджер автозапуска программ IceWM
позволяет путем установки rpm расширений просто настраивать 
рабочий стол IceWM по умолчанию сразу для всех пользователей, 
сохраняя за пользователями полную свободу персональной настройки
автозапуска.

Имеющиеся модули позволяют при старте icewm обновлять локальное меню пользователя
(если у него оно есть), запускать ivman, gkrellm, xxkb,
запускать рабочий стол (idesk, xtdesktop, desklaunch, kdesktop) и т. д.

%package delay
Group: Graphical desktop/Icewm
Summary: delay before starting programs
Summary(ru_RU.UTF-8): задержка запуска программ
Requires: %name
AutoReq: no

%description delay
delay before starting programs, to eliminate possible artifacts,
typically used to have time to start icewmtray.
%description -l ru_RU.UTF-8 delay
задержка перед запуском программ, чтобы устранить возможные артефакты,
обычно используется, чтобы успел стартовать icewmtray.

%package gkrellm
Group: Graphical desktop/Icewm
Summary: gkrellm autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск gkrellm при старте IceWM
# xtoolwait is required because icewm is not launched yet
Requires: %name gkrellm xtoolwait
AutoReq: no

%description gkrellm
gkrellm plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 gkrellm
запуск gkrellm при старте IceWM
(Требует менеджер автозапуска программ IceWM).

%package idesk
Group: Graphical desktop/Icewm
Summary: idesk autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск idesk при старте IceWM
Requires: %name idesk
Conflicts: %name-kdesktop
AutoReq: no

%description idesk
idesk plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 idesk
idesk plug-in для менеджера автозапуска программ при старте IceWM.

%package xxkb
Group: Graphical desktop/Icewm
Summary: xxkb autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xxkb при старте IceWM
Requires: %name xxkb
AutoReq: no
Conflicts: %name-xxkb-tray

%description xxkb
xxkb plug-in for simple pluggable IceWM autostart manager.
~/.xxkbrc or /etc/X11/app-defaults/XXkb is required.
%description -l ru_RU.UTF-8 xxkb
xxkb plug-in для менеджера автозапуска программ при старте IceWM.
Плагин запускает xxkb только при наличии ~/.xxkbrc или 
/etc/X11/app-defaults/XXkb.

%package xxkb-tray
Group: Graphical desktop/Icewm
Summary: xxkb autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск xxkb при старте IceWM
Requires: %name xxkb
AutoReq: no
Conflicts: %name-xxkb

%description xxkb-tray
xxkb plug-in for simple pluggable IceWM autostart manager.
~/.xxkbrc or /etc/X11/app-defaults/XXkb is required.
When you install package the file /etc/X11/app-defaults/XXkb
will be overwritten, and after removing returned to the old file.
%description -l ru_RU.UTF-8 xxkb-tray
xxkb plug-in для менеджера автозапуска программ при старте IceWM.
Плагин запускает xxkb только при наличии ~/.xxkbrc или 
/etc/X11/app-defaults/XXkb.
При установке пакета файл /etc/X11/app-defaults/XXkb будет
перезаписан, а после удаления возвращен старый файл.

%package ivman
Group: Graphical desktop/Icewm
Summary: ivman autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск ivman при старте IceWM
Requires: %name ivman
AutoReq: no

%description ivman
ivman plug-in for simple pluggable IceWM autostart manager.
%description -l ru_RU.UTF-8 ivman
ivman plug-in для менеджера автозапуска программ IceWM.

%package update-menus
Group: Graphical desktop/Icewm
Summary: autoupdate of user menu at IceWM startup
Summary(ru_RU.UTF-8): автообновление меню пользователя при старте IceWM (при необходимости)
Requires: %name menu
AutoReq: no

%description update-menus
update-menus plug-in for simple pluggable IceWM autostart manager.
Does autoupdate of user menu at IceWM startup. (~/.icewm/menu).

%description -l ru_RU.UTF-8 update-menus
update-menus plug-in для менеджера автозапуска программ IceWM.
автообновление меню пользователя при старте IceWM. 
Автообновление запускается только если пользователь 
не пользуется общесистемным меню, а предпочитает 
локальное меню из ~/.icewm/menu.

%package networkmanager
Group: Graphical desktop/Icewm
Summary: start gnome networkmanager applet
Requires: %name ModemManager NetworkManager-applet-gtk
Requires: NetworkManager-wifi usb-modeswitch
AutoReq: no

%description networkmanager
networkmanager plug-in for simple network configuration.
Start gnome networkmanager applet into tray.

%package tray_mixer_plus
Group: Graphical desktop/Icewm
Summary: start simple tray sound volume control
Requires: %name tray_mixer_plus
AutoReq: no

%description tray_mixer_plus
tray_mixer_plus plug-in for simple sound volume control.

%package grun
Group: Graphical desktop/Icewm
Summary: setup Run dialog
Requires: %name grun
AutoReq: no

%description grun
grun plug-in for setup dialog of launching applications in console mode.

%package simple-sound
Group: Graphical desktop/Icewm
Summary: Startup and shutdown simple sound for IceWM
Summary(ru_RU.UTF-8): Простейшие звуки при старте и выключении IceWM
Requires: %name aplay
AutoReq: no

%description simple-sound
Startup and shutdown simple sound for IceWM.
%description -l ru_RU.UTF-8 simple-sound
Простейшие звуки при старте и выключении IceWM.

%package xscreensaver
Group: Graphical desktop/Icewm
Summary: Startup xscreensaver for IceWM
Summary(ru_RU.UTF-8): Запуск xscreensaver при старте IceWM
Requires: %name xscreensaver xscreensaver-frontend
AutoReq: no

%description xscreensaver
Startup xscreensaver for IceWM.
%description -l ru_RU.UTF-8 xscreensaver
Автозапуск xscreensaver при старте IceWM.

%package mount-tray
Group: Graphical desktop/Icewm
Summary: mount-tray autostart at IceWM startup
Summary(ru_RU.UTF-8): автозапуск mount-tray при старте IceWM
Requires: %name mount-tray
AutoReq: no

%description -l ru_RU.UTF-8 mount-tray
Автозапуск mount-tray (автомонтирование USB устройств) при старте IceWM.


%prep
%setup -q -c -T

%build

cat > README.ru_RU.UTF-8 <<EOF

~/.icewm/startup_d

# starting all system-wide icewm autostart programs
for file in %icewmconfdir/startup_d/*; do
  userfile=~/.icewm/startup_d/`echo $file | sed -e 's,%icewmconfdir/startup_d/,,'`
  # root can disable autostart removing 'execute' bits
  if [ -x $file ]; then 
    # User-supplied programs disable system-wide programs.
    # So user can disable system-wide program 
    # by touching file in ~/.icewm/startup.d/ with the same name
    # or even replace it with his own script.

    # skip system-wide program if user-supplied file exists.
    [ -e $userfile ] || . $file
  fi
done

# starting user-supplied icewm autostart programs
for file in ~/.icewm/startup_d/*; do
  # running user files 
  # user can disable autostart removing 'execute' bits
  [ -x $file ] && . $file
done

EOF

%install
%__mkdir_p %buildroot%icewmconfdir/startup_d
%__mkdir_p %buildroot%icewmconfdir/shutdown_d
%__mkdir_p %buildroot%icewmconfdir/reboot_d
%__mkdir_p %buildroot%icewmconfdir/restart_d
%__mkdir_p %buildroot%icewmconfdir/logout_d

tar xf %SOURCE0 -C %buildroot%_datadir/

cat <<'EOF' > %buildroot%icewmconfdir/startup_d/001-delay
#!/bin/sh
# delay before starting programs, to eliminate possible artifacts
# name index 010- to save ability to run programs before this
tmem=`free -m | awk '/Mem/{print $2}'`
    if [ $tmem -le 512 ]
	then delay=7
    elif [ $tmem -gt 1024 ]
	then delay=3
    else delay=5
    fi
sleep $delay
EOF

cat <<EOF > %buildroot%icewmconfdir/startup_d/002-update-menus
#!/bin/sh
# if user has no local menu we will not create it either.
# otherwise it is worth updating it.
if [ -e ~/.icewm/menu ]; then
    update-menus &
fi
EOF

echo 'xtoolwait gkrellm'> %buildroot%icewmconfdir/startup_d/010-gkrellm

echo 'ivman&'> %buildroot%icewmconfdir/startup_d/020-ivman

cat <<EOF > %buildroot%icewmconfdir/startup_d/030-idesk
#!/bin/sh
idesk &
EOF

echo "xscreensaver -no-splash &" > %buildroot%icewmconfdir/startup_d/040-xscreensaver

cat <<EOF > %buildroot%icewmconfdir/startup_d/090-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/default/startup.wav ]; then
	aplay ~/.icewm/sounds/default/startup.wav 2&> /dev/null&
else
    if [ -e /usr/share/icewm/sounds/default/startup.wav ]; then
	aplay /usr/share/icewm/sounds/default/startup.wav 2&> /dev/null&
    fi
fi
EOF

cat <<EOF > %buildroot%icewmconfdir/shutdown_d/090-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/default/shutdown.wav ]; then
	aplay ~/.icewm/sounds/default/shutdown.wav 2&> /dev/null&
else
    if [ -e /usr/share/icewm/sounds/default/shutdown.wav ]; then
	aplay /usr/share/icewm/sounds/default/shutdown.wav 2&> /dev/null&
    fi
fi
EOF

cat <<EOF > %buildroot%icewmconfdir/restart_d/090-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/default/restart.wav ]; then
	aplay ~/.icewm/sounds/default/restart.wav 2&> /dev/null&
else
    if [ -e /usr/share/icewm/sounds/default/restart.wav ]; then
	aplay /usr/share/icewm/sounds/default/restart.wav 2&> /dev/null&
    fi
fi
EOF

cat <<EOF > %buildroot%icewmconfdir/reboot_d/090-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/default/restart.wav ]; then
	aplay ~/.icewm/sounds/default/restart.wav 2&> /dev/null&
else
    if [ -e /usr/share/icewm/sounds/default/restart.wav ]; then
	aplay /usr/share/icewm/sounds/default/restart.wav 2&> /dev/null&
    fi
fi
EOF

cat <<EOF > %buildroot%icewmconfdir/logout_d/090-simple-sound
#!/bin/sh

if [ -e ~/.icewm/sounds/default/shutdown.wav ]; then
	aplay ~/.icewm/sounds/default/shutdown.wav 2&> /dev/null&
else
    if [ -e /usr/share/icewm/sounds/default/shutdown.wav ]; then
	aplay /usr/share/icewm/sounds/default/shutdown.wav 2&> /dev/null&
    fi
fi
EOF

install -pD -m 644 %SOURCE1 %buildroot%_datadir/xxkb/XXkb.conf
cat <<EOF > %buildroot%icewmconfdir/startup_d/100-xxkb
#!/bin/sh
# it is not wise to run non-configured xxkb, so we look 
# whether it is configured.
# if [ -e ~/.xxkbrc ] then user has configured xxkb properly
# if [ -e /etc/X11/app-defaults/XXkb ]
# then sysadmin has configured xxkb properly.

if [ -e ~/.xxkbrc ] || [ -e /etc/X11/app-defaults/XXkb ]; then
  sleep 1
  xxkb&
fi
EOF

cp %buildroot%icewmconfdir/startup_d/100-xxkb %buildroot%icewmconfdir/startup_d/100-xxkb-tray

cat <<EOF > %buildroot%icewmconfdir/startup_d/110-tray_mixer_plus
#!/bin/sh

sleep 1
tray_mixer_plus&
EOF

cat <<EOF > %buildroot%icewmconfdir/startup_d/120-mount-tray
#!/bin/sh

sleep 1
mount-tray&
EOF

cat <<EOF > %buildroot%icewmconfdir/startup_d/140-networkmanager
#!/bin/sh

sleep 1
/usr/libexec/polkit-1/polkit-gnome-authentication-agent-1&
/usr/bin/nm-applet&
EOF

chmod 755 %buildroot%icewmconfdir/startup_d/*
chmod 755 %buildroot%icewmconfdir/shutdown_d/*
chmod 755 %buildroot%icewmconfdir/reboot_d/*
chmod 755 %buildroot%icewmconfdir/restart_d/*
chmod 755 %buildroot%icewmconfdir/logout_d/*

%post xxkb-tray
if [ $1 -eq 1 ]; then
    if [ -e %_x11appconfdir/XXkb ]; then
	cp -fp %_x11appconfdir/XXkb %_datadir/xxkb/XXkb~
	cp -fp %_datadir/xxkb/XXkb.conf %_x11appconfdir/XXkb
    fi
fi

%post grun
if [ $1 -eq 1 ]; then
echo "RunCommand=\"grun\"" >> %icewmconfdir/prefoverride
fi

%preun xxkb-tray
if [ $1 -eq 0 ]; then
    if [ -e %_datadir/xxkb/XXkb~ ]; then
	mv -f %_datadir/xxkb/XXkb~ %_x11appconfdir/XXkb
    else
	rm -f %_x11appconfdir/XXkb
    fi
fi

%preun grun
if [ $1 -eq 0 ]; then
    sed -i '/RunCommand=\"grun\"/d' %icewmconfdir/prefoverride
    if [ "`wc -w %icewmconfdir/prefoverride | cut -d" " -f1`" == "0" ]; then
	rm -f %icewmconfdir/prefoverride
    fi
fi

%files
%dir %icewmconfdir/startup_d
%dir %icewmconfdir/shutdown_d
%dir %icewmconfdir/reboot_d
%dir %icewmconfdir/restart_d
%dir %icewmconfdir/logout_d

%files delay
%config %icewmconfdir/startup_d/001-delay

%files update-menus
%config %icewmconfdir/startup_d/002-update-menus

%files gkrellm
%config %icewmconfdir/startup_d/010-gkrellm

%files ivman
%config %icewmconfdir/startup_d/020-ivman

%files idesk
%config %icewmconfdir/startup_d/030-idesk

%files xscreensaver
%config %icewmconfdir/startup_d/040-xscreensaver

%files simple-sound
%config %icewmconfdir/startup_d/090-simple-sound
%config %icewmconfdir/shutdown_d/090-simple-sound
%config %icewmconfdir/reboot_d/090-simple-sound
%config %icewmconfdir/restart_d/090-simple-sound
%config %icewmconfdir/logout_d/090-simple-sound
%dir %icewmconfdir/sounds
%icewmconfdir/sounds

%files xxkb
%config %icewmconfdir/startup_d/100-xxkb

%files xxkb-tray
%config %icewmconfdir/startup_d/100-xxkb-tray
%_datadir/xxkb/XXkb.conf

%files tray_mixer_plus
%config %icewmconfdir/startup_d/110-tray_mixer_plus

%files mount-tray
%config %icewmconfdir/startup_d/120-mount-tray

%files networkmanager
%config %icewmconfdir/startup_d/140-networkmanager

%files grun

%changelog
* Sat Mar 01 2016 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt8
- edit idesk

* Sat Dec 23 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt7
- new version

* Sat Dec 20 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt6.1
- add conflicts

* Sat Dec 14 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt6
- new version

* Sat Dec 07 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt5
- edit script mount-tray

* Sat Dec 06 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt4
- edit update-menus simpki-sound

* Sat Dec 04 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt3
- init git

* Sat Dec 03 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt3
- edit sleep in script xxkb mount-tray tray_mixer_plus networkmanager

* Sat Dec 02 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt2
- edit step run script

* Sat Nov 29 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.16-alt1.1
- delete xtdesktop desklaunch kdesktop startup shutdown
- add xscreensaver

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added mount-tray subpackage

* Sat Sep 26 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.15-alt2
- updated requires for networkmanager subpackage

* Sun May 31 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.15-alt1
- added "shutdown" script, thx to YYY at forum
- added simple-sound subpackage, thx to YYY and Leo-sp150 at forum
- delay moved to separate subpackage
- cosmetic fix of xxkb conf file
- some programs are assigned numeric indexes
- changed Url: and Packager:

* Mon Feb 09 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt3
- fixed typo in networkmanager subpackage

* Tue May 14 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt2
- delay before starting programs made customizable

* Wed Apr 10 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.14-alt1
- added grun subpackage

* Sat Mar 30 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.13-alt1
- added xxkb-tray subpackage
- added tray_mixer_plus subpackage
- spec converted to utf-8

* Thu Feb 28 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.12-alt1
- added delay before starting programs, to eliminate possible artifacts
- added networkmanager

* Wed Mar 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3
- removed artsd support (obsolete)

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1
- disabled unmet subpackages using nmu script

* Fri Sep 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- fixed requires in update-menus

* Thu Sep 20 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added arts, update-menus
- TODO: README

* Sat Sep 08 2007 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- added ivman, desklaunch and xtdesktop support

* Mon Apr 17 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt2
- added kdesktop support

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt1
- build for Sisyphus

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0.M30.1
- backport for M30

* Wed Mar 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.0-alt0
- initial build
