Summary:	Lightweight volume control
Name:		volumeicon
Version:	0.5.0
Release:	2
License:	GPL v3
Group:		X11/Applications
#Source0:	http://softwarebakery.com/maato/files/volumeicon/%{name}-%{version}.tar.gz
Source0:	https://github.com/Maato/volumeicon/archive/master.zip
# Source0-md5:	90163045427369a229ea1faca906741e
URL:		http://softwarebakery.com/maato/volumeicon.html
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight volume control.

%prep
%setup -qn %{name}-master

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/volumeicon
%{_datadir}/%{name}
%{_desktopdir}/volumeicon.desktop
%{_sysconfdir}/xdg/autostart/volumeicon.desktop

