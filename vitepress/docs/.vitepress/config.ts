import { defineConfig } from "vitepress";

export default defineConfig({
	title: "DobotAPI",
	description: "Python package for controlling Dobot Magician and it's addons",
	lang: "en-US",
	base: "https://stax124.github.io/DobotAPI/",
	appearance: true,
	lastUpdated: true,
	outDir: "../../docs",
	themeConfig: {
		sidebar: [
			{
				text: "Introduction",
				items: [
					{ text: "Introduction", link: "/" },
					{ text: "Installation", link: "/installation" },
					{ text: "Getting started", link: "/getting-started" },
				],
				collapsible: true,
			},
			{
				text: "Addons",
				items: [
					{ text: "Effectors", link: "/addons/effectors" },
					{ text: "Conveyor belt", link: "/addons/conveyor-belt" },
					{ text: "Engraver", link: "/addons/engraver" },
				],
				collapsible: true,
			},
			{
				text: "Shell",
				items: [
					{ text: "Position", link: "/shell/position" },
					{ text: "Effectors", link: "/shell/effectors" },
					{ text: "Conveyor belt", link: "/shell/conveyor-belt" },
				],
				collapsible: true,
			},
		],
		editLink: {
			pattern:
				"https://github.com/Stax124/DobotAPI/edit/main/vitepress/docs/:path",
		},
	},
});
