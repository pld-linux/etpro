%define _ver	%(echo %{version} | tr . _)
Summary:	Enemy Territory - ETpro
Summary(pl):	Enemy Territory (Terytorium wroga) ETpro
Name:		etpro
Version:	3.1.0
Release:	0.4
Epoch:		0
License:	as-is
Group:		Applications/Games
Source0:	http://bani.anime.net/etpro/etpro-%{_ver}.zip
# Source0-md5:	e2e47a25f92e4824a742832c2bca7c51
Source1:	%{name}.desktop
URL:		http://bani.anime.net/etpro/
BuildRequires:	unzip
Requires:	et
Requires:	et-data
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1
%define		no_install_post_chrpath 1
%define		_gamelibdir	%{_libdir}/games/et
%define		_gamedatadir	%{_datadir}/games/et

%description
Enemy Territory - ETpro.

%description -l pl
Enemy Territory (Terytorium wroga) ETpro.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},{%{_gamelibdir},%{_gamedatadir}}/etpro}

cat << EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
# Needed to make symlinks/shortcuts work.
# the binaries must run with correct working directory
cd %{_gamelibdir}
exec ./et +set fs_game etpro "\$@"
EOF

cp -a animations configs etpromapscripts maps $RPM_BUILD_ROOT%{_gamelibdir}/etpro

install *.pk3 $RPM_BUILD_ROOT%{_gamedatadir}/etpro
ln -s ../../../../share/games/et/etpro/etpro-%{_ver}.pk3 $RPM_BUILD_ROOT%{_gamelibdir}/etpro

install etpro_cheats.dat example.cfg $RPM_BUILD_ROOT%{_gamelibdir}/etpro
install *.so $RPM_BUILD_ROOT%{_gamelibdir}/etpro

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_gamelibdir}/etpro
%attr(755,root,root) %{_gamelibdir}/etpro/*.so
%{_gamelibdir}/etpro/etpro_cheats.dat
%{_gamelibdir}/etpro/animations
%{_gamelibdir}/etpro/configs
%{_gamelibdir}/etpro/etpromapscripts
%{_gamelibdir}/etpro/maps
%{_gamelibdir}/etpro/*.cfg
%{_gamelibdir}/etpro/*.pk3
%dir %{_gamedatadir}/etpro
%{_gamedatadir}/etpro/*.pk3
%{_desktopdir}/%{name}.desktop
