Summary:	SHN plugin for XMMS
Summary(pl):	Wtyczka dla XMMS-a odtwarzaj�ca pliki SHN
Name:		xmms-input-shn
Version:	2.2.8
Release:	0.1
License:	SHORTEN SOFTWARE LICENSE
Group:		X11/Applications/Sound
Source0:	http://www.etree.org/shnutils/xmms-shn/source/xmms-shn-%{version}.tar.gz
# Source0-md5:	9f74c510fe2a21c22d30443af82b31ab
URL:		http://www.etree.org/shnutils/xmms-shn/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows XMMS to play SHN files.

%description -l pl
Ta wtyczka pozwala XMMS-owi odtwarza� muzyk� w formacie SHN.

%prep
%setup -q -n xmms-shn-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS doc/*
%attr(755,root,root) %{xmms_input_plugindir}/*
