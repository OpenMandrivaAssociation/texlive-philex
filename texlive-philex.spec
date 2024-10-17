Name:		texlive-philex
Version:	36396
Release:	2
Summary:	Cross references for named and numbered environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/philex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Philex provides means for creating and cross-referencing named
or numbered environments. Possible uses would be equations,
example sentences (as in linguistics or philosophy) or named
principles. Cross references may refer either to the number, or
to a short name of the target environment, or to the contents
of the environment. Philex builds on the facilities of the
linguex package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/philex
%doc %{_texmfdistdir}/doc/latex/philex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
