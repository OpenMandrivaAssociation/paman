%define name paman
%define version 0.9.4
%define release 11
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
BuildRequires: pkgconfig(libglademm-2.4)
BuildRequires: pulseaudio-devel >= 0.9.7
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-8mdv2011.0
+ Revision: 666984
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-7mdv2011.0
+ Revision: 607067
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-6mdv2010.1
+ Revision: 523569
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.4-5mdv2010.0
+ Revision: 426355
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.9.4-4mdv2009.0
+ Revision: 218433
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 31 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.4-4mdv2008.1
+ Revision: 160891
- Fix %%postun (#37210)

* Wed Jan 16 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.4-3mdv2008.1
+ Revision: 153757
- Move to System menu rather than Sound.
- Fix %%post[un] macros

* Tue Jan 15 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.4-2mdv2008.1
+ Revision: 151984
- Add icons for x-desktop use (MDV#36579)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.4-1mdv2008.1
+ Revision: 103907
- New version


* Mon Feb 05 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.3-1mdv2007.0
+ Revision: 116257
- Import paman

* Mon Aug 28 2006 Götz Waschk <waschk@mandriva.org> 0.9.3-1mdv2007.0
- bump deps
- New release 0.9.3

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2007.0
- rebuild for new cairomm

* Tue Jul 11 2006 Götz Waschk <waschk@mandriva.org> 0.9.2-2mdv2007.0
- fix buildrequires

* Tue Jul 11 2006 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2007.0
- update patch
- update deps
- New release 0.9.2

* Sat Jun 17 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-2mdv2007.0
- no need to update the desktop database
- fix menu
- fix buildrequires

* Tue Jun 06 2006 Jerome Soyer <saispo@mandriva.org> 0.9.1-1mdv2007.0
- Fix title and longtitle in Menu
- New release 0.9.1

* Mon Jun 05 2006 Jerome Soyer <saispo@mandriva.org> 0.9.0-2mdv2007.0
- Add menu entry but no icons provided
- Fix BuildRequires and Requires

* Mon Jun 05 2006 Jerome Soyer <saispo@mandriva.org> 0.9.0-1mdv2007.0
- Initial Package for Mandriva

