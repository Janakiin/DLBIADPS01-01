<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:output method="html" encoding="UTF-8" indent="yes"/>

	<xsl:template match="/">
		<html>
			<head>
				<title>Filme im Kino</title>
				<style>
					.title { font-size: 24px; font-weight: bold; }
					.director { font-size: 18px; font-style: italic; }
					.movie { margin-bottom: 20px; }
				</style>
			</head>
			<body>
				<h1>Filme im Kino</h1>
				<xsl:for-each select="movies/movie">
					<div class="movie">
						<div class="title">
							<xsl:value-of select="title"/>
						</div>
						<div class="director">
							Regisseur: <xsl:value-of select="director"/>
						</div>
						<div class="genre">
							Genre: <xsl:value-of select="genre"/>
						</div>
						<div class="releaseDate">
							Erscheinungsdatum: <xsl:value-of select="releaseDate"/>
						</div>
						<div class="rating">
							Bewertung: <xsl:value-of select="rating"/>
						</div>
					</div>
				</xsl:for-each>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>