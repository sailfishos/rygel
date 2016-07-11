Name:          rygel
Version:       0.25.3
Release:       1%{?dist}
Summary:       A collection of UPnP/DLNA services

Group:         Applications/Multimedia
License:       LGPLv2+
URL:           http://live.gnome.org/Rygel
Source0:       ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/0.20/%{name}-%{version}.tar.xz

BuildRequires: gnome-common
BuildRequires: gobject-introspection-devel >= 1.36
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
#BuildRequires: pkgconfig(gstreamer-1.0)
#BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: gupnp-devel
BuildRequires: gupnp-av-devel
BuildRequires: gupnp-dlna-devel
BuildRequires: libgee-devel
BuildRequires: libsoup-devel
#BuildRequires: libunistring-devel
BuildRequires: libuuid-devel
BuildRequires: sqlite-devel
BuildRequires: tracker-devel
BuildRequires: pkgconfig(libmediaart-2.0)
BuildRequires: intltool
Obsoletes: rygel-gst-plugins

%description
Rygel is a home media solution that allows you to easily share audio, video and
pictures, and control of media player on your home network. In technical terms
it is both a UPnP AV MediaServer and MediaRenderer implemented through a plug-in
mechanism. Interoperability with other devices in the market is achieved by
conformance to very strict requirements of DLNA and on the fly conversion of
media to format that client devices are capable of handling.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package tracker
Summary: Tracker plugin for %{name}
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: tracker

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
echo -n %{version} > .version
echo -n %{version} > .tarball-version
%autogen release --enable-tracker-plugin --disable-silent-rules --with-media-engine=simple --disable-strict-valac

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

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
%config %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_libdir}/librygel*.so.*
%{_libdir}/rygel-2.6/engines/*
%{_libdir}/rygel-2.6/plugins/external.plugin
%{_libdir}/rygel-2.6/plugins/librygel-external.so
%{_libdir}/rygel-2.6/plugins/librygel-mpris.so
%{_libdir}/rygel-2.6/plugins/mpris.plugin
%{_libdir}/rygel-2.6/plugins/librygel-ruih.so
%{_libdir}/rygel-2.6/plugins/ruih.plugin
#%{_libdir}/rygel-2.6/plugins/librygel-media-export.so
#%{_libdir}/rygel-2.6/plugins/librygel-playbin.so
#%{_libdir}/rygel-2.6/plugins/media-export.plugin
#%{_libdir}/rygel-2.6/plugins/playbin.plugin
%{_libdir}/girepository-1.0/RygelCore-2.6.typelib
%{_libdir}/girepository-1.0/RygelRenderer-2.6.typelib
%{_libdir}/girepository-1.0/RygelServer-2.6.typelib
%{_datadir}/rygel/
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service

%files tracker
%{_libdir}/rygel-2.6/plugins/librygel-tracker.so
%{_libdir}/rygel-2.6/plugins/tracker.plugin

%files devel
%{_libdir}/librygel-*.so
%{_includedir}/rygel-2.6
%{_libdir}/pkgconfig/rygel*.pc
%{_datadir}/vala/vapi/rygel-*
%{_datadir}/gir-1.0/RygelCore-2.6.gir
%{_datadir}/gir-1.0/RygelRenderer-2.6.gir
%{_datadir}/gir-1.0/RygelServer-2.6.gir
