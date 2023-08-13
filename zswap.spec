Name: zswap
Summary: Init, set up & stats for zswap
Summary(ru_RU.UTF-8): Служба настройки, запуска и вывода статистики zswap
Url: https://github.com/Smoque/zswap

Version: 0.51
Release: alt1
License: GPLv2
Group: System/Configuration/Hardware

BuildArch: noarch

# Author Author: Vadim A. Illarionov
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar

%description
zswap init, set up & stats.

%description -l ru_RU.UTF8
Настройка, запуск и вывод статистики zswap.

%prep
%setup
%__subst s\\'$version'\\"%version"\\ %name.service

%install
install  -Dm 755 %name           %buildroot%_bindir/%name
install  -Dm 755 %name.init      %buildroot%_initdir/%name
install -pDm 644 %name.service   %buildroot%_unitdir/%name.service
install -pDm 644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -pDm 644 -t              %buildroot%_docdir/%name-%version/ README.*
install -pDm 644 C               %buildroot%_datadir/%name/C
install -pDm 644 ru_RU.UTF-8     %buildroot%_datadir/%name/ru_RU.UTF-8

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc README.ru_RU.UTF-8 README.md
%_datadir/%name/C
%_datadir/%name/ru_RU.UTF-8
%_unitdir/%name.service
%_initdir/%name
%_bindir/%name

%changelog
* Sat Aug 12 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.51-alt1
- Fixed stats output to the journald

* Fri Aug 11 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.50-alt1
- version 0.50

* Fri Aug 11 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.45-alt1
- Added detection of debian forks

* Thu Aug 10 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.40-alt1
- Added reload function

* Mon Jul 31 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.21-alt1
- Added russian translation and runtime options

* Wed Jul 26 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.20-alt1
- Added russian documentation

* Fri Jul 21 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.11-alt1
- Initial build to Sisyphus

* Thu Jul 20 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.10-alt1
- Initial build
