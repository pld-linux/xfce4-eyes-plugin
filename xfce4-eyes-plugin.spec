Summary:	A eyes plugin for Xfce panel
Summary(pl.UTF-8):	Wtyczka eyes dla panelu Xfce
Name:		xfce4-eyes-plugin
Version:	4.4.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-eyes-plugin/4.4/%{name}-%{version}.tar.bz2
# Source0-md5:	1ef352c68dd8929c9e8743200b758b3c
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.9.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin adds eyes to the Xfce panel which watch user every step.

%description -l pl.UTF-8
Ta wtyczka dodaje do panelu Xfce oczy, które patrzą na każdy krok
użytkownika.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libeyes.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libeyes.so
%{_datadir}/xfce4/panel/plugins/eyes.desktop
%{_datadir}/xfce4/eyes
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
