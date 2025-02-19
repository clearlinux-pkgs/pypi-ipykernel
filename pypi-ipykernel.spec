#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: 4ea76c9
#
Name     : pypi-ipykernel
Version  : 6.29.5
Release  : 139
URL      : https://files.pythonhosted.org/packages/e9/5c/67594cb0c7055dc50814b21731c22a601101ea3b1b50a9a1b090e11f5d0f/ipykernel-6.29.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/5c/67594cb0c7055dc50814b21731c22a601101ea3b1b50a9a1b090e11f5d0f/ipykernel-6.29.5.tar.gz
Summary  : IPython Kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-ipykernel-data = %{version}-%{release}
Requires: pypi-ipykernel-license = %{version}-%{release}
Requires: pypi-ipykernel-python = %{version}-%{release}
Requires: pypi-ipykernel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(ipython)
BuildRequires : pypi(jupyter_client)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(pexpect)
BuildRequires : pypi(platformdirs)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pyzmq)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# IPython Kernel for Jupyter
[![Build Status](https://github.com/ipython/ipykernel/actions/workflows/ci.yml/badge.svg?query=branch%3Amain++)](https://github.com/ipython/ipykernel/actions/workflows/ci.yml/badge.svg?query=branch%3Amain++)
[![Documentation Status](https://readthedocs.org/projects/ipykernel/badge/?version=latest)](http://ipykernel.readthedocs.io/en/latest/?badge=latest)

%package data
Summary: data components for the pypi-ipykernel package.
Group: Data

%description data
data components for the pypi-ipykernel package.


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
Requires: pypi(comm)
Requires: pypi(debugpy)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(jupyter_core)
Requires: pypi(matplotlib_inline)
Requires: pypi(nest_asyncio)
Requires: pypi(packaging)
Requires: pypi(psutil)
Requires: pypi(pyzmq)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-ipykernel package.


%prep
%setup -q -n ipykernel-6.29.5
cd %{_builddir}/ipykernel-6.29.5
pushd ..
cp -a ipykernel-6.29.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730173535
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipykernel
cp %{_builddir}/ipykernel-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ipykernel/e1b5dbe8939a03fbd08dca727e41562ccd59b6e3 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/logo-64x64.png
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/logo-32x32.png
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/kernel.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/kernels/python3/logo-svg.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipykernel/e1b5dbe8939a03fbd08dca727e41562ccd59b6e3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
