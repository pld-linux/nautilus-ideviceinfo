Summary:	Nautilus Property Page for iPhone/iPod Touch/iPad devices
Name:		nautilus-ideviceinfo
Version:	0.1.0
Release:	10
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	cf31bc0ffec70b33c87483f379bbdcf5
Patch0:		%{name}-gtk3.patch
Patch1:		%{name}-mobile-broadband-db-path.patch
URL:		https://git.gnome.org/browse/nautilus-ideviceinfo
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.14.1
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool
BuildRequires:	libgpod-devel >= 0.7.90
BuildRequires:	libimobiledevice-devel >= 0.9.7
BuildRequires:	libplist-devel >= 0.15
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.30
BuildRequires:	mobile-broadband-provider-info-devel >= 20100510-2
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
Requires:	libgpod >= 0.7.90
Requires:	mobile-broadband-provider-info
Requires:	nautilus >= 3.0.0
Requires:	usbmuxd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-iDeviceInfo is a nautilus extension showing extended device
information in the nautilus properties dialog. It shows details like
serial number, software version, baseband/modem firmware version, and
storage usage (with nice eye candy).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/*.so
%{_libdir}/nautilus/extensions-3.0/*.ui
