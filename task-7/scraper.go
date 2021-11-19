package main

import (
	"github.com/PuerkitoBio/goquery"
	"github.com/geziyor/geziyor"
	"github.com/geziyor/geziyor/client"
	"github.com/geziyor/geziyor/export"
)

func main() {
	geziyor.NewGeziyor(&geziyor.Options{
		StartRequestsFunc: func(g *geziyor.Geziyor) {
			g.GetRendered("https://www.forbes.com/real-time-billionaires/#7cc167ea3d78", g.Opt.ParseFunc)
		},
		ParseFunc: quotesParse,
		Exporters: []export.Exporter{&export.JSON{}},
	}).Start()
}

func quotesParse(g *geziyor.Geziyor, r *client.Response) {
	r.HTMLDoc.Find("#row-4 > div.table-parent > div > div.fbs-table > div.scrolly-table > table > tbody > tr:nth-child(-n+10)").Each(func(i int, s *goquery.Selection) {
		g.Exports <- map[string]interface{}{
			"name":                 s.Find("td.name > div > h3 > a").Text(),
			"net_worth":            s.Find("td.Net.Worth > div > span").Text(),
			"age":                  s.Find("td.age > div > span").Text(),
			"source_of_income":     s.Find("td.source > div > span").Text(),
			"country_or_territory": s.Find("td[class*=\"Country\"] > div > span").Text(),
		}
	})
}
