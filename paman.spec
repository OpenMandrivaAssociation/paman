Summary:	Manager for Pulseaudio sound server for Linux
Name:		paman
Version:	0.9.4
Release:	14
License:	LGPLv2
Group:		Sound
Url:		http://0pointer.de/lennart/projects/paman
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Patch0:		paman-0.9.2-typo.patch
BuildRequires:	desktop-file-utils
BuildRequires:	lynx
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libpulse)
Requires:	pulseaudio
Provides:	pulseaudio-manager

%description
A simple GTK frontend for the pulseaudio sound server

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="GTK" \
	--add-category="System" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Icons
install -D -m 0644 %SOURCE1 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 0644 %SOURCE2 %{buildroot}%{_iconsdir}/%{name}.png

%files
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png

