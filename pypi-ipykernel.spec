#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipykernel
Version  : 6.9.0
Release  : 91
URL      : https://files.pythonhosted.org/packages/b5/0a/0948dbf21a15810ecb27d229199cd7248cf068c73ad9be42e0610a7dba79/ipykernel-6.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/0a/0948dbf21a15810ecb27d229199cd7248cf068c73ad9be42e0610a7dba79/ipykernel-6.9.0.tar.gz
Summary  : IPython Kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: pypi-ipykernel-license = %{version}-%{release}
Requires: pypi-ipykernel-python = %{version}-%{release}
Requires: pypi-ipykernel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(debugpy)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(ipython)
BuildRequires : pypi(jupyter_client)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(matplotlib_inline)
BuildRequires : pypi(nest_asyncio)
BuildRequires : pypi(pexpect)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tornado)
BuildRequires : pypi(traitlets)
BuildRequires : pypi(wheel)

%description
# IPython Kernel for Jupyter
This package provides the IPython kernel for Jupyter.

%package license
Summary: license components for the pypi-ipykernel package.
Group: Default

%description license
license components for the pypi-ipykernel package.


%package python
Summary: python components for the pypi-ipykernel package.
Group: Default
Requires: pypi-ipykernel-python3 = %{version}-%{release}

%description python
python components for the pypi-ipykernel package.


%package python3
Summary: python3 components for the pypi-ipykernel package.
Group: Default
Requires: python3-core
Provides: pypi(ipykernel)
Requires: pypi(debugpy)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(matplotlib_inline)
Requires: pypi(nest_asyncio)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-ipykernel package.


%prep
%setup -q -n ipykernel-6.9.0
cd %{_builddir}/ipykernel-6.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644279367
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipykernel
cp %{_builddir}/ipykernel-6.9.0/COPYING.md %{buildroot}/usr/share/package-licenses/pypi-ipykernel/a8d9e56558dabe10c8e716d79a4b01dcb6cf950f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/logo-64x64.png
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/logo-32x32.png
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/kernel.json

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipykernel/a8d9e56558dabe10c8e716d79a4b01dcb6cf950f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
