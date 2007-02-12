Summary:	SHN plugin for XMMS
Summary(pl.UTF-8):   Wtyczka wejściowa dla XMMS-a odtwarzająca pliki SHN
Name:		xmms-input-shn
Version:	2.4.0
Release:	0.1
License:	SHORTEN SOFTWARE LICENSE
Group:		X11/Applications/Sound
Source0:	http://www.etree.org/shnutils/xmms-shn/source/xmms-shn-%{version}.tar.gz
# Source0-md5:	00395ac407b6b9d5e2c48ad4bbb324f7
URL:		http://www.etree.org/shnutils/xmms-shn/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows XMMS to play SHN files.

%description -l pl.UTF-8
Ta wtyczka pozwala XMMS-owi odtwarzać muzykę w formacie SHN.

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
