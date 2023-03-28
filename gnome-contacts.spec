#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-contacts
Version  : 44.0
Release  : 34
URL      : https://download.gnome.org/sources/gnome-contacts/44/gnome-contacts-44.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-contacts/44/gnome-contacts-44.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-contacts-bin = %{version}-%{release}
Requires: gnome-contacts-data = %{version}-%{release}
Requires: gnome-contacts-libexec = %{version}-%{release}
Requires: gnome-contacts-license = %{version}-%{release}
Requires: gnome-contacts-locales = %{version}-%{release}
Requires: gnome-contacts-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : docbook-xml
BuildRequires : evolution-data-server-dev
BuildRequires : folks-dev
BuildRequires : gnome-online-accounts-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : pkgconfig(folks)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libportal-gtk4)
BuildRequires : pkgconfig(libqrencode)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# GNOME Contacts
Contacts organizes your contacts information from all your online and offline
sources, providing a centralized place for managing your contacts.

%package bin
Summary: bin components for the gnome-contacts package.
Group: Binaries
Requires: gnome-contacts-data = %{version}-%{release}
Requires: gnome-contacts-libexec = %{version}-%{release}
Requires: gnome-contacts-license = %{version}-%{release}

%description bin
bin components for the gnome-contacts package.


%package data
Summary: data components for the gnome-contacts package.
Group: Data

%description data
data components for the gnome-contacts package.


%package libexec
Summary: libexec components for the gnome-contacts package.
Group: Default
Requires: gnome-contacts-license = %{version}-%{release}

%description libexec
libexec components for the gnome-contacts package.


%package license
Summary: license components for the gnome-contacts package.
Group: Default

%description license
license components for the gnome-contacts package.


%package locales
Summary: locales components for the gnome-contacts package.
Group: Default

%description locales
locales components for the gnome-contacts package.


%package man
Summary: man components for the gnome-contacts package.
Group: Default

%description man
man components for the gnome-contacts package.


%prep
%setup -q -n gnome-contacts-44.0
cd %{_builddir}/gnome-contacts-44.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680027813
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
target=$HOME/.local/share/glib-2.0/schemas
mkdir -p $target
glib-compile-schemas --targetdir=$target /usr/share/glib-2.0/schemas
export XDG_DATA_DIRS="$HOME/.local/share${XDG_DATA_DIRS:+:$XDG_DATA_DIRS}"
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-contacts
cp %{_builddir}/gnome-contacts-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-contacts/2c026582eb07be6897378e91a8c8c76fee512d72 || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-contacts

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-contacts

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Contacts.desktop
/usr/share/dbus-1/services/org.gnome.Contacts.SearchProvider.service
/usr/share/dbus-1/services/org.gnome.Contacts.service
/usr/share/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Contacts.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Contacts.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Contacts-symbolic.svg
/usr/share/metainfo/org.gnome.Contacts.appdata.xml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-contacts-search-provider
/usr/libexec/gnome-contacts/gnome-contacts-parser

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-contacts/2c026582eb07be6897378e91a8c8c76fee512d72

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-contacts.1

%files locales -f gnome-contacts.lang
%defattr(-,root,root,-)

