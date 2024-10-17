#imported from MRB

%define version 0.8.99
%define release %mkrel 0.%revision.1
#newer svn 
%define revision 1323046

Name:		kftpgrabber
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:	        https://www.kftp.org/	
Group:		Networking/File transfer
Source0:		%{name}-%version.%revision.tar.bz2
Patch0:		kftpgrabber-0.8.99.1323046-ssh2.patch
Summary:        Graphical FTP client for KDE4
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



%files
%doc AUTHORS ChangeLog COPYING README Roadmap
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

%files -n %libkftpinterfaces
%doc AUTHORS ChangeLog COPYING README Roadmap
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
%doc AUTHORS ChangeLog COPYING README Roadmap
%_kde_libdir/libkftpinterfaces.so

#------------------------------------------------


%prep
%setup -q -n kftpgrabber-0.8.99.1323046
%patch0 -p1 -b ssh2-fix

%build
%cmake_kde4 
%make

%install
cd build
%{makeinstall_std}
cd .
chmod 644 %buildroot/%_kde_datadir/applications/kde4/kftpgrabber.desktop



