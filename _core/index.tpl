<!DOCTYPE html>
<html lang="en">
<head>
    <title>SuperPython</title>
    <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="utf-8">
    <!--script type="text/javascript" src="https://j.mp/brython_371"></script -->
    <script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.4.0/brython.min.js">
    </script>
    <script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.4.0/brython_stdlib.js">
    </script>
    <link rel="stylesheet"
          href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/default.min.css">
    <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>
    <script type="text/python">
            import julia.main
            julia.main.main()

    </script>

    <!--
    #! /usr/bin/env python
    # -*- coding: UTF8 -*-
    # Este arquivo é parte do programa Kwarwp
    # Copyright 2010-2018 Carlo Oliveira <carlo@nce.ufrj.br>,
    # `Labase <http://labase.selfip.org/>`__; `GPL <http://j.mp/GNU_GPL3>`__.
    #
    # Kwarwp é um software livre; você pode redistribuí-lo e/ou
    # modificá-lo dentro dos termos da Licença Pública Geral GNU como
    # publicada pela Fundação do Software Livre (FSF); na versão 2 da
    # Licença.
    #
    # Este programa é distribuído na esperança de que possa ser útil,
    # mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
    # a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
    # Licença Pública Geral GNU para maiores detalhes.
    #
    # Você deve ter recebido uma cópia da Licença Pública Geral GNU
    # junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

    """Brython front end client.

    .. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

    """

    -->
</head>
<body onLoad="brython({debug:1, cache:'browser', static_stdlib_import:true,
 pythonpath :['__code']})">
<div id="pydiv">
</div>
</body>
</html>
