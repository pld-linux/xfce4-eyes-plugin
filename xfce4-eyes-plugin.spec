Summary:	A eyes plugin for Xfce panel
Summary(pl.UTF-8):	Wtyczka eyes dla panelu Xfce
Name:		xfce4-eyes-plugin
Version:	4.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-eyes-plugin/4.7/%{name}-%{version}.tar.xz
# Source0-md5:	3ce7965b7d6a1cd921c41514860b4ee5
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-eyes-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
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

mkdir -p m4

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hy_AM
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hye
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie
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
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libeyes.so
%{_datadir}/xfce4/panel/plugins/eyes.desktop
%{_datadir}/xfce4/eyes
%{_iconsdir}/hicolor/*/apps/xfce4-eyes.png
