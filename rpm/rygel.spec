%global apiver  2.6

Name:          rygel
Version:       0.36.2
Release:       1
Summary:       A collection of UPnP/DLNA services

License:       LGPLv2+
URL:           https://wiki.gnome.org/Projects/Rygel
Source0:       %{name}-%{version}.tar.xz
Patch0:        0001-Constructors-of-abstract-classes-should-not-be-publi.patch
Patch1:        0001-renderer-Fix-type-argument-mismatch.patch
Patch2:        0001-build-Add-additional-GIR-tweak-for-references-to-Ryg.patch

BuildRequires: gobject-introspection-devel >= 1.36
BuildRequires: desktop-file-utils
#BuildRequires: pkgconfig(gstreamer-1.0)
#BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(systemd)
BuildRequires: gupnp-devel >= 0.20.14
BuildRequires: gupnp-av-devel
BuildRequires: gupnp-dlna-devel
BuildRequires: libgee-devel
BuildRequires: libsoup-devel
#BuildRequires: libunistring-devel
BuildRequires: libuuid-devel
BuildRequires: sqlite-devel
BuildRequires: tracker-devel
BuildRequires: pkgconfig(libmediaart-2.0)
BuildRequires: gettext
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
echo -n %{version} > .version
echo -n %{version} > .tarball-version
%autogen release --enable-tracker-plugin --disable-silent-rules --with-media-engine=simple --disable-strict-valac --disable-lms-plugin --disable-example-plugins

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
%license COPYING
%config %{_sysconfdir}/rygel.conf
%{_bindir}/rygel
%{_libdir}/librygel*.so.*
%{_libdir}/rygel-%{apiver}/engines/*
%{_libdir}/rygel-%{apiver}/plugins/external.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-external.so
%{_libdir}/rygel-%{apiver}/plugins/librygel-mpris.so
%{_libdir}/rygel-%{apiver}/plugins/mpris.plugin
%{_libdir}/rygel-%{apiver}/plugins/librygel-ruih.so
%{_libdir}/rygel-%{apiver}/plugins/ruih.plugin
%{_libdir}/girepository-1.0/RygelCore-%{apiver}.typelib
%{_libdir}/girepository-1.0/RygelRenderer-%{apiver}.typelib
%{_libdir}/girepository-1.0/RygelServer-%{apiver}.typelib
%{_datadir}/rygel/
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_libdir}/systemd/user/rygel.service

%files tracker
%license COPYING
%{_libdir}/rygel-%{apiver}/plugins/librygel-tracker.so
%{_libdir}/rygel-%{apiver}/plugins/tracker.plugin

%files devel
%{_libdir}/librygel-*.so
%{_includedir}/rygel-%{apiver}
%{_libdir}/pkgconfig/rygel*.pc
%{_datadir}/vala/vapi/rygel-*
%{_datadir}/gir-1.0/RygelCore-%{apiver}.gir
%{_datadir}/gir-1.0/RygelRenderer-%{apiver}.gir
%{_datadir}/gir-1.0/RygelServer-%{apiver}.gir
