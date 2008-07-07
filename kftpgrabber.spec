%define version 0.8.99
%define release %mkrel 0.%revision.1
%define revision 829080

Name:		kftpgrabber
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:	        http://www.kftp.org/	
Group:		Networking/File transfer
Source0:	%{name}-r%revision.tar.bz2
Summary:        Graphical FTP client for KDE4
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  openssl-devel
BuildRequires:	ssh2-devel
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
Obsoletes:  %{_lib}kftpgrabber0 < 0.8.1-2

%description -n %libkftpinterfaces
KFtpgrabber library.

%if %mdkversion < 200900
%post -n %libkftpinterfaces -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkftpinterfaces -p /sbin/ldconfig
%endif

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
%setup -q -n %name

%build
# otherwise it fails on linking final executable
%define _disable_ld_as_needed 1
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
