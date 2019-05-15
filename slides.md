% Plugin Content Curation for Quarterly Publication in Golden Slide Deck
% Kevin Putnam
% May 15, 2019

# Summary

Each quarter we will be updating the golden slide deck with the latest content from each of the supported plugins. In order to facilitate this process we are asking that each plugin team keep an up to date markdown file in their repository with only a summary and key takeaways for their plugin.

# Call to Action

We use pandoc 2.7 or newer to process the markdown. Instructions on the flavor of markdown used to generate the slides are available in the pandoc [manual](https://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc). 

In order for us to process it we will need:

1. URL (https) for cloning the repo
2. Full path to the markdown file (including filename) inside of the repo

# Building the Slides

You can use this presentation as a guide for creating your own presentation. 

We recommend building the slide presentation locally to verify that it renders as intended and that any included material like images shows up properly.

\ 

```bash
pandoc input-file-name.md -o output-file-name.pptx
```

# Final Product

Content from all of the repos will be collated into a master .pptx document and posted as part of a tagged release in our GitHub repository. 

# Examples

The following slides demonstrate the markdown syntax for a few useful formatting methods.

# Two column layout

:::::: {.columns}
::: {.column width="40%"}
Content of the left column.
:::

::: {.column width="60%"}
Content of the right column.
:::
::::::

------------------

![picture of spaghetti](spaghetti.jpg)