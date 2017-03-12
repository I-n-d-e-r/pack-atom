%global dat %{buildroot}%{_datadir}/%{name}/
%global bin %{buildroot}%{_bindir}/
%global sat %{_datadir}/%{name}/

%global out out/%{name}*/

%global apm %{sat}resources/app/apm/bin/apm
%global ato %{sat}%{name}

%global ico %{buildroot}%{_datadir}/icons/hicolor/
%global app %{buildroot}%{_datadir}/applications/

%global res resources/app-icons/stable/png/

Name:    atom
Version: 1.15.0
Release: 1%{?dist}
Summary: A hackable text editor for the 21st Century
URL: 	 https://atom.io/
License: MIT

Source0: https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

Requires: lsb-core-noarch
Requires: libXss.so.1()(64bit)

AutoReqProv: no

BuildRequires: libgnome-keyring-devel
BuildRequires: libX11-devel
BuildRequires: libxkbfile-devel

BuildRequires: nodejs
BuildRequires: npm
BuildRequires: git

%description
Atom is a text editor that's modern, approachable, yet hackable to the core—a tool
you can customize to do anything but also use productively without ever touching a config file.

%prep
%autosetup

%build
./script/build

%install
mkdir -p %{dat}
mkdir -p %{bin}
mkdir -p %{app}

mkdir -p %{ico}1024x1024/apps
mkdir -p %{ico}512x512/apps
mkdir -p %{ico}256x256/apps
mkdir -p %{ico}128x128/apps
mkdir -p %{ico}64x64/apps
mkdir -p %{ico}48x48/apps
mkdir -p %{ico}32x32/apps
mkdir -p %{ico}24x24/apps
mkdir -p %{ico}16x16/apps

cp -p -r %{out}* %{dat}

cp -p %{res}1024.png %{ico}1024x1024/apps/%{name}.png
cp -p %{res}512.png %{ico}512x512/apps/%{name}.png
cp -p %{res}256.png %{ico}256x256/apps/%{name}.png
cp -p %{res}128.png %{ico}128x128/apps/%{name}.png
cp -p %{res}64.png %{ico}64x64/apps/%{name}.png
cp -p %{res}48.png %{ico}48x48/apps/%{name}.png
cp -p %{res}32.png %{ico}32x32/apps/%{name}.png
cp -p %{res}24.png %{ico}24x24/apps/%{name}.png
cp -p %{res}16.png %{ico}16x16/apps/%{name}.png

ln -sf  %{apm} %{bin}
ln -sf  %{ato} %{bin}

%files
%{_bindir}/apm
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/

%changelog
* Sun Mar 12 2017 Dominik Opyd <dominik.opyd@gmail.com> 1.15.0-1
- Initial: Atom 1.15.0
