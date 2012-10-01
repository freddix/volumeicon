Summary:	Lightweight volume control
Name:		volumeicon
Version:	0.4.6
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://softwarebakery.com/maato/files/volumeicon/%{name}-%{version}.tar.gz
# Source0-md5:	7fd6dffba823e9c529d151d4789ff992
Patch0:		%{name}-include.patch
URL:		http://softwarebakery.com/maato/volumeicon.html
BuildRequires:	alsa-lib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight volume control.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-notify
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

