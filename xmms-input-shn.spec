Summary:	SHN plugin for xmms
Summary(pl):	Wtyczka odtwarzaj±ca pliki SHN dla xmms
Name:		xmms-input-shn
Version:	2.2.7
Release:	0.1
License:	SHORTEN SOFTWARE LICENSE
Group:		X11/Applications/Sound
Source0:	http://www.etree.org/shnutils/xmms-shn/source/xmms-shn-%{version}.tar.gz
URL:		http://www.etree.org/shnutils/xmms-shn/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	XFree86-devel
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_plugin_dir	%(xmms-config --input-plugin-dir)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This plugin allows xmms to play SHN files.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê w formacie SHN.

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

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS doc/*
%attr(755,root,root) %{_xmms_plugin_dir}/*
