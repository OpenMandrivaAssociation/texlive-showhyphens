# revision 23937
# category Package
# catalog-ctan /macros/luatex/latex/showhyphens
# catalog-date 2011-09-15 16:18:00 +0200
# catalog-license other-free
# catalog-version 0.1
Name:		texlive-showhyphens
Version:	0.1
Release:	1
Summary:	Show all possible hyphenations in LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/showhyphens
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphens.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphens.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
With this package, LuaLaTeX will indicate all possible
hyphenations in the printed output.

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
%{_texmfdistdir}/tex/lualatex/showhyphens/showhyphens.sty
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/README
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-doc.pdf
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-doc.tex
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-sample.pdf
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
