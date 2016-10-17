#
# spec file for package skelcd-control-openSUSE-LangAddOn
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           skelcd-control-openSUSE-LangAddOn
# xmllint
BuildRequires:  libxml2-tools
# control.rng
BuildRequires:  yast2-installation-control
Url:            https://github.com/yast/skelcd-control-openSUSE-LangAddOn
AutoReqProv:    off
Version:        13.2.2
Release:        0
Summary:        skelcd for lang-addons
License:        GPL-2.0+
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2
Provides:       product_control
BuildArch:      noarch

%description
skelcd for lang-addons

# NOTE: Do not patch the installation.xml file in OBS, fork
# https://github.com/yast/skelcd-control-openSUSE-LangAddOn instead and create
# a pull request. The package is autosubmitted from Git by Jenkins CI
# (http://ci.opensuse.org/view/Yast/), your changes could be lost.

%prep

%setup -n %{name}-%{version}

%check
#
# Verify syntax
#
make -C control check

%install
#
# Add control file 
#
mkdir -p $RPM_BUILD_ROOT/CD1
install -m 644 control/installation.xml $RPM_BUILD_ROOT/CD1/installation.xml

%files
%defattr(644,root,root,755)
/CD1

%changelog
