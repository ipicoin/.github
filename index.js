
// import root from './translations/i18n.json'
// import en from './translations/EN/dictionary.json'
// import de from './translations/DE/dictionary.json'
// import pl from './translations/PL/dictionary.json'
// import es = await import('./translations/ES/dictionary.json'
// const ru = await import('./translations/RU/dictionary.json'
// const ua = await import('./translations/UA/dictionary.json', {
//   with: { type: 'json' },
// })
// const ro = await import('./translations/RO/dictionary.json', {
//   assert: { type: 'json' },
// })
import { createRequire } from 'node:module';


const LANGCHAIN = "en-de-pl-es-ru-ua-ro"


const LOCALES = Object.assign(
    {
        messages: Object.fromEntries(
            new Map(
                LANGCHAIN.split(
                    "-"
                ).map(
                    (x)=>(
                        [
                            x,
                            createRequire(
                                import.meta.url
                            )(
                                `./translations/${x.toUpperCase()}/dictionary.json`
                            )
                        ]
                    )
                )
            )
        )
    },createRequire(
        import.meta.url
    )(
        './translations/i18n.json'
    )
)
//console.log(LOCALES)

export default LOCALES