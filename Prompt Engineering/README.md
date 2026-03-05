System Prompt:

You are an analyst. This is a review: "DePrima's heroine seems a little out of sync, comparing Miss Bumbling from the Academy with Captain Ferocious of the Prometheus, but I guess all that time in stasis renders more dreams than any researchers ever guessed. Or something. Or else the author has really screwed up, and based on the rest of his writing, I don't think that happened." Kindly derive the following things from this review: Title (concise and descriptive) Summary (23 sentences maximum) Sentiments (strictly one of: positive, negative, neutral) Keywords (meaningful phrases (not random words)) Confidence_score (float between 0.0 and 1.0.) Note: No markdown wrapping, No explanations. Output format: JSON




Input example 1:

"DePrima's heroine seems a little out of sync, comparing Miss Bumbling from the Academy with Captain Ferocious of the Prometheus, but I guess all that time in stasis renders more dreams than any researchers ever guessed. Or something. Or else the author has really screwed up, and based on the rest of his writing, I don't think that happened."

Output example 1:

{
"Title": "Unusual Character Comparison but Confidence in Author’s Skill",
"Summary": "The reviewer finds the heroine’s characterization somewhat out of sync due to an unusual comparison with other characters. They suggest the inconsistency might be explained by the effects of long stasis, ultimately trusting the author's competence rather than assuming it is a mistake.",
"Sentiments": "positive",
"Keywords": ["heroine characterization", "character comparison", "stasis explanation", "author competence", "narrative interpretation"],
"Confidence_score": 0.84
}




Input example 2:

The notebook I bought is nice but very ordinary. The paper quality is acceptable and the size fits in my bag. It’s fine for everyday notes but nothing special.

Output example 2:

{
"Title": "Ordinary Notebook Suitable for Everyday Use",
"Summary": "The reviewer finds the notebook decent but unremarkable. While the paper quality and size are acceptable for daily notes, it does not offer anything distinctive or impressive.",
"Sentiments": "neutral",
"Keywords": ["notebook quality", "ordinary design", "paper quality acceptable", "portable size", "everyday note-taking"],
"Confidence_score": 0.93
}




Input example 3:

I ordered a kitchen knife and it arrived dull, which was disappointing. After sharpening it myself it works better, but I feel like that shouldn’t be necessary. Packaging was also pretty basic.

Output example 3:

{
"Title": "Kitchen Knife Arrives Dull but Improves After Sharpening",
"Summary": "The reviewer was disappointed that the kitchen knife arrived dull and required sharpening before it could be used effectively. Although it performs better after sharpening, the reviewer believes this extra step should not have been necessary and also notes the basic packaging.",
"Sentiments": "negative",
"Keywords": ["dull kitchen knife", "required sharpening", "product quality issue", "basic packaging", "initial disappointment"],
"Confidence_score": 0.94
}
