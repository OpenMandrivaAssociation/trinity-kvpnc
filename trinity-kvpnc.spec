%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg kvpnc
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	0.9.6a
Release:	%{?tde_version:%{tde_version}_}3
Summary:	Vpn clients frontend for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/internet/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# ACL support
BuildRequires:  pkgconfig(libacl)

# GCRYPT support
BuildRequires:  pkgconfig(libgcrypt) >= 1.2.0

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
KVpnc is a TDE frontend for various vpn clients.

It supports :
* Cisco-compatible VPN client (vpnc)
* IPSec (freeswan, openswan, racoon)
* Point-to-Point Tunneling Protocol (PPTP) client (pptp-linux)
* Virtual Private Network daemon (openvpn)


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.md TODO
%{tde_prefix}/bin/kvpnc
%{tde_prefix}/share/applications/tde/kvpnc.desktop
%{tde_prefix}/share/apps/kvpnc/
%lang(de) %{tde_prefix}/share/doc/tde/HTML/de/kvpnc/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/kvpnc/
%lang(fr) %{tde_prefix}/share/doc/tde/HTML/fr/kvpnc/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/kvpnc/
%{tde_prefix}/share/icons/hicolor/*/apps/kvpnc.png
%{tde_prefix}/share/icons/locolor/*/apps/kvpnc.png
%{tde_prefix}/share/doc/kvpnc/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/pcf/
%{tde_prefix}/share/services/pcf.protocol
%{tde_prefix}/share/man/man1/*.1*

