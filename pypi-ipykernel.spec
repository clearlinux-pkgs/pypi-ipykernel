#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-ipykernel
Version  : 6.25.2
Release  : 122
URL      : https://files.pythonhosted.org/packages/8b/4a/3c1ba010e1517191eefb9f2fc556a3aed146b8c4e65708aed3ad17e803c5/ipykernel-6.25.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/4a/3c1ba010e1517191eefb9f2fc556a3aed146b8c4e65708aed3ad17e803c5/ipykernel-6.25.2.tar.gz
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
BuildRequires : pypi(python_dateutil)
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
%setup -q -n ipykernel-6.25.2
cd %{_builddir}/ipykernel-6.25.2
pushd ..
cp -a ipykernel-6.25.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693931938
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipykernel
cp %{_builddir}/ipykernel-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ipykernel/e1b5dbe8939a03fbd08dca727e41562ccd59b6e3 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
