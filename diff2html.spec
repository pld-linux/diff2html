Summary:	diff2html - utility generates an HTML page to display the output of the diff
Summary(fr):	L'utilitaire diff2html g�n�re une page HTML valide pour afficher le r�sultat de l'utilitaire bien connu diff
Summary(pl):	diff2html - narz�dzie generuj�ce stron� HTML wy�wietlaj�c� wyj�cie narz�dzia diff
Name:		diff2html
Version:	1.0.1
Release:	0.1
License:	GPL
Group:		Applications/Text
Source0:	http://kafka.fr.free.fr/diff2html/diff2html.bz2
# Source0-md5:	e3aa3bd4fec0a93f5f97efcd210e232b
URL:		http://kafka.fr.free.fr/diff2html/
Requires:	python
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The diff2html utility generates an HTML page to display the output of
the diff(1) well-known utility. Using Cascading Style Sheets, the user
can fully personalize the appearance of the web page (you might find
the default styles are too much colorful).

%description -l fr
L'utilitaire diff2html g�n�re une page HTML valide pour afficher le
r�sultat de l'utilitaire bien connu diff. Par l'utilisation des
feuilles de styles CSS2, l'utilisateur peut compl�tement personnaliser
l'apparence de la page web (vous pouvez estimer que les styles par
d�faut sont trop color�s). diff2html est �crit en langage Python et
est soumis � la license GNU GPL.

%description -l pl
narz�dzie diff2html generuje stron� HTML wy�wietlaj�c� wyj�cie innego
dobrze znanego narz�dzia diff. U�ywaj�c kaskadowych styl�w (CSS) mo�na
w pe�ni spersonalizowa� wygl�d strony.

%prep
%setup -q -c -T
install %{SOURCE0} .
bunzip2 %{name}.bz2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
