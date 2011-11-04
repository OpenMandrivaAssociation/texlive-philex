# revision 17879
# category Package
# catalog-ctan /macros/latex/contrib/philex
# catalog-date 2010-04-29 12:33:30 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-philex
Version:	1.0
Release:	1
Summary:	Cross references for named and numbered environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/philex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/philex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Philex provides means for creating and cross-referencing named
or numbered environments. Possible uses would be equations,
example sentences (as in linguistics or philosophy) or named
principles. Cross references may refer either to the number, or
to a short name of the target environment, or to the contents
of the environment. Philex builds on the facilities of the
linguex package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/philex/philex.sty
%doc %{_texmfdistdir}/doc/latex/philex/philexmanualb.pdf
%doc %{_texmfdistdir}/doc/latex/philex/philexmanualb.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
