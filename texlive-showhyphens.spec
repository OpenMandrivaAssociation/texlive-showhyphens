# revision 23937
# category Package
# catalog-ctan /macros/luatex/latex/showhyphens
# catalog-date 2011-09-15 16:18:00 +0200
# catalog-license other-free
# catalog-version 0.1
Name:		texlive-showhyphens
Version:	0.5c
Release:	4
Summary:	Show all possible hyphenations in LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/showhyphens
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphens.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphens.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With this package, LuaLaTeX will indicate all possible
hyphenations in the printed output.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/showhyphens/showhyphens.sty
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/README
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-doc.pdf
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-doc.tex
%doc %{_texmfdistdir}/doc/lualatex/showhyphens/showhyphens-sample.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 755985
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719528
- texlive-showhyphens
- texlive-showhyphens
- texlive-showhyphens
- texlive-showhyphens

