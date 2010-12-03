%define name paman
%define version 0.9.4
%define release %mkrel 7
%define title Pulseaudio Manager
%define longtitle Manager for Pulseaudio sound server for Linux

Summary: Manager for Pulseaudio sound server for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-16.png
Source2: %{name}-32.png
Patch: paman-0.9.2-typo.patch
License: LGPL
Group: Sound
Url: http://0pointer.de/lennart/projects/paman
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkmm2.4-devel
BuildRequires: libglademm-devel
BuildRequires: libpulseaudio-devel >= 0.9.7
BuildRequires: lynx
BuildRequires: desktop-file-utils
Requires: pulseaudio

Provides: pulseaudio-manager

%description
A simple GTK frontend for the pulseaudio sound server

%prep
%setup -q
%patch -p1 -b .typo

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="System" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

# Icons
install -D -m 0644 %SOURCE1 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 0644 %SOURCE2 %{buildroot}%{_iconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_desktop_database
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_desktop_database
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png


