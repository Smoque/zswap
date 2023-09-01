Name:		zswap
Version:	0.53
Release:	alt1
License:	GPLv3
Group:		System/Configuration/Hardware
BuildArch:	noarch
Url:		https://github.com/Smoque/zswap
Source:		%url/releases/download/v%version/%name-%version.tar
Requires:	awk bc grep sed
Summary:	Init, set up & stats for zswap
Summary(ru_RU.UTF-8): Служба настройки, запуска и вывода статистики zswap

%description
zswap init, set up & stats.

%description -l ru_RU.UTF8
Настройка, запуск и вывод статистики zswap.

%prep
%setup
%__subst s\\'$version'\\"%version"\\ %name.service

%install
install  -Dm 755 %name         %buildroot%_sbindir/%name
install  -Dm 755 %name.init    %buildroot%_initdir/%name
install -pDm 644 %name.service %buildroot%_unitdir/%name.service
install -pDm 644 %name.syscfg  %buildroot%_sysconfdir/sysconfig/%name
install -pDm 644 ru_RU.UTF-8   %buildroot%_datadir/%name/ru_RU.UTF-8
install -pDm 644 -t            %buildroot%_docdir/%name-%version/ README.*

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc README.ru_RU.UTF-8 README.md
%_datadir/%name/ru_RU.UTF-8
%_unitdir/%name.service
%_initdir/%name
%_sbindir/%name

%changelog
* Fri Sep 01 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.53-alt1
- minor bugfixes

* Wed Aug 23 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.52-alt1
- script rewrite

* Thu Aug 17 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.51-alt1
- fixed status output to the journald

* Sat Aug 12 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.50-alt1
- fixed status output to the journald

* Wed Aug 07 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.40-alt1
- debian detection
- reload capability

* Wed Aug 02 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.30-alt1
- russian localization

* Thu Jul 20 2023 Vadim A. Illarionov <gbIMoBou@ya.ru> 0.1-alt1
- initial build
