
Name:          rygel
Version:       0.40.1
Release:       1
Summary:       A collection of UPnP/DLNA services

License:       LGPLv2+
URL:           https://wiki.gnome.org/Projects/Rygel
Source0:       %{name}-%{version}.tar.xz
Patch0:        0001-Completely-disable-doc-generation-because-we-dont-ha.patch

BuildRequires: pkgconfig
BuildRequires: meson
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libmediaart-2.0)
BuildRequires: pkgconfig(gupnp-1.2)
BuildRequires: pkgconfig(gupnp-av-1.0)
BuildRequires: pkgconfig(gupnp-dlna-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(tracker-sparql-3.0)
BuildRequires: gettext
BuildRequires: desktop-file-utils

%description
Rygel is a home media solution that allows you to easily share audio, video and
pictures, and control of media player on your home network. In technical terms
it is both a UPnP AV MediaServer and MediaRenderer implemented through a plug-in
mechanism. Interoperability with other devices in the market is achieved by
conformance to very strict requirements of DLNA and on the fly conversion of
media to format that client devices are capable of handling.

%package devel
Summary: Development package for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package tracker
Summary: Tracker plugin for %{name}
Requires: %{name} = %{version}-%{release}
Requires: tracker

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dplugins=tracker3,external,mpris,ruih -Dexamples=false -Dgtk=disabled -Dengines=simple -Dgstreamer=disabled -Dtests=false
%meson_build

%install
%meson_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

rm %{buildroot}/%{_datadir}/applications/rygel.desktop
rm %{buildroot}/%{_datadir}/applications/rygel-preferences.desktop
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/*/apps/rygel*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%config %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_libdir}/librygel*.so.*
%{_libdir}/rygel-*/engines/*
%{_libdir}/rygel-*/plugins/external.plugin
%{_libdir}/rygel-*/plugins/librygel-external.so
%{_libdir}/rygel-*/plugins/librygel-mpris.so
%{_libdir}/rygel-*/plugins/mpris.plugin
%{_libdir}/rygel-*/plugins/librygel-ruih.so
%{_libdir}/rygel-*/plugins/ruih.plugin
%{_libdir}/girepository-1.0/RygelCore-*.typelib
%{_libdir}/girepository-1.0/RygelRenderer-*.typelib
%{_libdir}/girepository-1.0/RygelServer-*.typelib
%{_datadir}/rygel/
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_userunitdir}/rygel.service

%files tracker
%license COPYING
%{_libdir}/rygel-*/plugins/librygel-tracker3.so
%{_libdir}/rygel-*/plugins/tracker3.plugin

%files devel
%{_libdir}/librygel-*.so
%{_includedir}/rygel-*
%{_libdir}/pkgconfig/rygel*.pc
%{_datadir}/vala/vapi/rygel-*
%{_datadir}/gir-1.0/RygelCore-*.gir
%{_datadir}/gir-1.0/RygelRenderer-*.gir
%{_datadir}/gir-1.0/RygelServer-*.gir
