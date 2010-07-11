# TODO
#   Show mobile carrier:  no
Summary:	Nautilus Property Page for iPhone/iPod Touch/iPad devices
Name:		nautilus-ideviceinfo
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
URL:		http://git.gnome.org/browse/nautilus-ideviceinfo
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	cf31bc0ffec70b33c87483f379bbdcf5
BuildRequires:	gnome-desktop-devel
BuildRequires:	intltool
BuildRequires:	libgpod-devel >= 0.7.90
BuildRequires:	libimobiledevice-devel >= 0.9.7
BuildRequires:	libxml2-devel >= 2.6.30
BuildRequires:	nautilus-devel
Requires:	libgpod >= 0.7.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-iDeviceInfo is a nautilus extension showing extended device
information in the nautilus properties dialog. It shows details like
serial number, software version, baseband/modem firmware version, and
storage usage (with nice eye candy).

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.*a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/nautilus/extensions-2.0/*.so
%{_libdir}/nautilus/extensions-2.0/*.ui
