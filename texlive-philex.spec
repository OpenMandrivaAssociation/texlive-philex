# revision 33315
# category Package
# catalog-ctan /macros/latex/contrib/philex
# catalog-date 2014-03-28 20:06:26 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-philex
Version:	1.2
Release:	3
Summary:	Cross references for named and numbered environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/philex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philex.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/philex/philex.sty
%doc %{_texmfdistdir}/doc/latex/philex/README
%doc %{_texmfdistdir}/doc/latex/philex/README.rtf
%doc %{_texmfdistdir}/doc/latex/philex/philexmanual.pdf
%doc %{_texmfdistdir}/doc/latex/philex/philexmanual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
