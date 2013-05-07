Summary:	Lightweight volume control
Name:		volumeicon
Version:	0.5.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://softwarebakery.com/maato/files/volumeicon/%{name}-%{version}.tar.gz
# Source0-md5:	3ed1c8995331da888fd45e06896a7569
URL:		http://softwarebakery.com/maato/volumeicon.html
BuildRequires:	alsa-lib-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight volume control.

%prep
%setup -q

%build
%configure \
	--enable-notify
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/xdg/autostart,%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_desktopdir}/volumeicon.desktop <<EOF
[Desktop Entry]
Name=Volume Icon
Comment=Lightweight volume control
Icon=audio-volume-high-panel
Exec=volumeicon
Terminal=false
Type=Application
Categories=Utility;
NoDisplay=true
OnlyShowIn=XFCE;OPENBOX;
EOF

ln -s %{_desktopdir}/volumeicon.desktop \
	$RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/volumeicon
%{_datadir}/%{name}
%{_desktopdir}/volumeicon.desktop
%{_sysconfdir}/xdg/autostart/volumeicon.desktop

