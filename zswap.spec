Name:      zswap
Version:   0.5
Release:   alt1
License:   GPL
Group:     System/Configuration/Hardware
Url:       https://github.com/Smoque/zswap
BuildArch: noarch
Summary:   zswap init, set up & stats
Source0:   %name
Source1:   %name.init
Source2:   %name.service
Source3:   %name.sysconfig
Source4:   LICENSE
Source5:   README.md
Source6:   README.ru_RU.UTF-8
Source7:   ru_RU.UTF-8
Source8:   C

%description
zswap init, set up & stats.

%description(ru_RU.UTF8)
Настройка, запуск/выключение и статистика zswap.

%install
install  -Dm 755 %SOURCE0 %buildroot%_bindir/%name
install  -Dm 755 %SOURCE1 %buildroot%_initdir/%name
install -pDm 644 %SOURCE2 %buildroot%_unitdir/%name.service
install -pDm 644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -pDm 644 %SOURCE4 %buildroot%_docdir/%name/LICENSE
install -pDm 644 %SOURCE5 %buildroot%_docdir/%name/README.md
install -pDm 644 %SOURCE6 %buildroot%_docdir/%name/README.ru_RU.UTF-8
install -pDm 644 %SOURCE7 %buildroot%_datadir/%name/ru_RU.UTF-8
install -pDm 644 %SOURCE8 %buildroot%_datadir/%name/C

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%_datadir/%name/C
%_datadir/%name/ru_RU.UTF-8
%_docdir/%name/README.ru_RU.UTF-8
%_docdir/%name/README.md
%_docdir/%name/LICENSE
%_unitdir/%name.service
%_initdir/%name
%_bindir/%name

%changelog
* Fri Aug 11 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.5-alt1
- Debian forks detection added
* Thu Aug 10 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.4-alt1
- reload added
* Wed Aug 09 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.3-alt1
- default and translated messages moved to /usr/share/zswap/
* Mon Jul 31 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.2-alt1
- russian translation and runtime options added
* Thu Jul 20 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.1-alt1
- initial build
