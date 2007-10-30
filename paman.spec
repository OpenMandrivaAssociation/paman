%define name paman
%define version 0.9.4
%define release %mkrel 1
%define title Pulseaudio Manager
%define longtitle Manager for Pulseaudio sound server for Linux

Summary: Manager for Pulseaudio sound server for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE
%_bindir/%name
%_datadir/%name/%name.glade
%_datadir/applications/%name.desktop


