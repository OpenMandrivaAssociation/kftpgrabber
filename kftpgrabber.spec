%define version 0.8.99
%define release %mkrel 0.%revision.4
%define revision 741976

Name:		kftpgrabber
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:	        http://kftpgrabber.sourceforge.net/	
Group:		Networking/File transfer
Source0:	%{name}-%version.%revision.tar.bz2
Summary:        Graphical FTP client for KDE4
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  openssl-devel
Obsoletes:      kde4-%name <= 0.8.99-0.741976.4
Provides:       kde4-%name

Requires: kdebase4-runtime

%description
KFTPGrabber is a graphical FTP client for KDE4.
It supports SSL encryption, FXP transfers,
multiple FTP sessions (using tabs), bookmark system and more.

%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor

%files
%defattr(-,root,root)
%_kde_bindir/kftpgrabber
%_kde_libdir/kde4/kftpimportplugin_filezilla3.so
%_kde_libdir/kde4/kftpimportplugin_gftp.so
%_kde_libdir/kde4/kftpimportplugin_kftp.so
%_kde_libdir/kde4/kftpimportplugin_ncftp.so
%_kde_datadir/applications/kde4/kftpgrabber.desktop
%_kde_appsdir/kftpgrabber/commands.xml
%_kde_appsdir/kftpgrabber/kftpgrabber-bi-wizard.png
%_kde_appsdir/kftpgrabber/kftpgrabber-logo.png
%_kde_appsdir/kftpgrabber/kftpgrabberui.rc
%_kde_iconsdir/hicolor/*/apps/kftpgrabber.png
%_kde_datadir/kde4/services/kftpbookmarkimportplugin.desktop
%_kde_datadir/kde4/services/kftpimportplugin_filezilla3.desktop
%_kde_datadir/kde4/services/kftpimportplugin_gftp.desktop
%_kde_datadir/kde4/services/kftpimportplugin_kftp.desktop
%_kde_datadir/kde4/services/kftpimportplugin_ncftp.desktop

#------------------------------------------------

%define libkftpinterfaces %mklibname kftpinterfaces 4

%package -n %libkftpinterfaces
Summary: KDE 4 core library
Group: System/Libraries


%description -n %libkftpinterfaces
KFtpgrabber library.

%post -n %libkftpinterfaces -p /sbin/ldconfig
%postun -n %libkftpinterfaces -p /sbin/ldconfig

%files -n %libkftpinterfaces
%defattr(-,root,root)
%_kde_libdir/libkftpinterfaces.so.*

#------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KFtpgrabber based applications
Requires: %libkftpinterfaces = %version
Obsoletes:      kde4-%name-devel <= 0.8.99-0.741976.4
Provides:       kde4-%name-devel


%description devel
This package includes the header files you will need to compile applications
for KFtpgrabber.

%files devel
%defattr(-,root,root,-)
%_kde_libdir/libkftpinterfaces.so

#------------------------------------------------


%prep
%setup -q -n %name-%version

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
