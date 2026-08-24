# Public Repository Audit

Assessment date: **2026-08-24**

This audit covers all **41 public repositories** in the `ipicoin` GitHub
organization. It distinguishes source that is IPI-specific from inherited
upstream code and records what the default branch actually demonstrates.

## Method

- Enumerated every public repository through the GitHub API.
- Inspected source trees, manifests, tests, workflows, licenses, and opening
  documentation for every original repository.
- Compared every GitHub fork against its declared upstream default branch.
- Ran available checks on the strongest original repositories using Node 24 or
  their documented local validators.
- Treated generated clients, configuration files, scaffolds, hosted endpoints,
  and target architecture as distinct kinds of evidence.

This is a presentation and source audit, not a security audit or certification.

## Original and imported source repositories

| Repository | What is in the source | IPI-specific evidence | Functional/maturity result |
| --- | --- | --- | --- |
| [`.github`](https://github.com/ipicoin/.github) | Governance, security, contribution policy, architecture, roadmap, IPI proposal process, validation script | Original public standards and evidence model | Active bootstrap process; community validation passes |
| [`scan.ipi.io`](https://github.com/ipicoin/scan.ipi.io) | Browser explorer, local API proxy, native Cosmos/CometBFT queries, EVM JSON-RPC diagnostics | Explorer routing, rendering, search, account, validator, block, transaction, and EVM inspection | Active development; syntax checks and public explorer CI pass |
| [`wallet-core.js`](https://github.com/ipicoin/wallet-core.js) | JavaScript models, controllers, wallet-operation scaffolds, seven test files | Wallet/address/request/transaction/contract models and configurable Bech32 validation | 11 tests pass; key import/generation and transfer paths are incomplete or broken and untested; high-severity audit remediation is in [PR #20](https://github.com/ipicoin/wallet-core.js/pull/20) |
| [`www.ipi.io`](https://github.com/ipicoin/www.ipi.io) | Astro landing page, small Starlight documentation tree, OpenSpec change record | IPI website and launch/documentation presentation | Static build passes on Node 24; dependency audit remediation is in [PR #11](https://github.com/ipicoin/www.ipi.io/pull/11) |
| [`chainconfig`](https://github.com/ipicoin/chainconfig) | One Cosmos wallet configuration export and one coherence test | Historical IPI chain metadata and Bech32/denomination fields | Test passes; values identify legacy `ipi-mainnet-2`, not a canonical current release |
| [`protocolix`](https://github.com/ipicoin/protocolix) | Capacitor Android/iOS projects and the default camera/demo web shell | IPI package/bundle identifiers and native project scaffold | Web scaffold builds and native project trees are checked in; no wallet, signing, NFC, or secure-key implementation and no application tests; audit and build CI pass in [PR #11](https://github.com/ipicoin/protocolix/pull/11) |
| [`ipi-rpc`](https://github.com/ipicoin/ipi-rpc) | Protobuf tree, two generated TypeScript client trees, Next.js comparison pages | Repository packaging and research framing | Upstream-derived integration sandbox; no IPI endpoints or RPC server implementation |
| [`Iswap`](https://github.com/ipicoin/Iswap) | Hyperweb swap example with Cosmos Kit and Osmosis query dependencies | Status, provenance, and IPI research framing only | Imported sandbox; no IPI configuration, tests, or public CI |
| [`Ivote`](https://github.com/ipicoin/Ivote) | Hyperweb governance proposal/vote example | Status, provenance, and IPI research framing only | Imported sandbox; no IPI configuration, tests, or public application CI |
| [`ipi-nft`](https://github.com/ipicoin/ipi-nft) | Hyperweb/Stargaze NFT example with mint, sale, transfer, and burn hooks | Status, provenance, and IPI research framing only | Imported sandbox; no IPI configuration, tests, or public application CI |
| [`ipicoin.github.io`](https://github.com/ipicoin/ipicoin.github.io) | Default Vue/Vite demo, placeholder counter store, one default Playwright test | Repository naming and legacy presentation only | Build passes; no IPI product behavior and no unit tests; canonical source is `www.ipi.io`; audit remediation is in [PR #10](https://github.com/ipicoin/ipicoin.github.io/pull/10) |
| [`hq-spacecraft`](https://github.com/ipicoin/hq-spacecraft) | Compose include skeleton, one Pi-hole definition, empty service files, placeholder Python/Task commands | Self-hosting research organization and documentation | Prototype skeleton; not a deployable collaboration stack |
| [`universal-independency-declaration`](https://github.com/ipicoin/universal-independency-declaration) | Empty JavaScript entry, hello-world Python/Rust, language manifests | Link to IPI-0001 research direction | Concept skeleton; no shared API, fixtures, or executable independence checks |
| [`standard_repo_template`](https://github.com/ipicoin/standard_repo_template) | Repository readiness README, Apache license, empty source/test placeholders | IPI publication and evidence checklist | Documentation template, not an implementation |

## Public forks and upstream delta

The table reports commits **ahead of the current upstream default branch** at
the assessment date. Zero means the fork contains no IPI-specific source change.

| Repository | Declared upstream | Ahead / behind | Role and finding |
| --- | --- | ---: | --- |
| [`independency-daemon`](https://github.com/ipicoin/independency-daemon) | `CosmWasm/wasmd` | 2 / 11 | Node research foundation; two IPI commits add provenance and fork-safe CI only, with no consensus/application changes |
| [`chain-registry`](https://github.com/ipicoin/chain-registry) | `cosmos/chain-registry` | 0 / 49 | Cosmos metadata reference; no IPI entry or modification in this fork |
| [`CosmWasm___cosmwasm`](https://github.com/ipicoin/CosmWasm___cosmwasm) | `CosmWasm/cosmwasm` | 0 / 1 | CosmWasm framework reference |
| [`CosmWasm___wasmvm`](https://github.com/ipicoin/CosmWasm___wasmvm) | `CosmWasm/wasmvm` | 0 / 0 | CosmWasm VM binding reference |
| [`CosmWasm___cosmwasm-contracts`](https://github.com/ipicoin/CosmWasm___cosmwasm-contracts) | `CosmWasm/cosmwasm-contracts` | 0 / 0 | Upstream contract test examples |
| [`cw-template`](https://github.com/ipicoin/cw-template) | `CosmWasm/cw-template` | 0 / 0 | Contract project template reference |
| [`hyperweb-io___starship`](https://github.com/ipicoin/hyperweb-io___starship) | `hyperweb-io/starship` | 0 / 0 | Interchain test-infrastructure reference |
| [`Agoric___agoric-sdk`](https://github.com/ipicoin/Agoric___agoric-sdk) | `Agoric/agoric-sdk` | 0 / 148 | JavaScript smart-contract platform reference |
| [`foundry-rs___foundry`](https://github.com/ipicoin/foundry-rs___foundry) | `foundry-rs/foundry` | 0 / 568 | EVM development tooling reference |
| [`argotorg___solidity`](https://github.com/ipicoin/argotorg___solidity) | `argotorg/solidity` | 0 / 144 | Solidity compiler reference |
| [`Uniswap___v4-core`](https://github.com/ipicoin/Uniswap___v4-core) | `Uniswap/v4-core` | 0 / 0 | AMM architecture reference; not an IPI liquidity implementation |
| [`foundry-rs___starknet-foundry`](https://github.com/ipicoin/foundry-rs___starknet-foundry) | `foundry-rs/starknet-foundry` | 0 / 49 | Starknet tooling reference; not part of a demonstrated IPI path |
| [`nikeee___node-ntag424`](https://github.com/ipicoin/nikeee___node-ntag424) | `nikeee/node-ntag424` | 0 / 18 | Working upstream NTAG 424 library reference; no IPI integration |
| [`Yubico___yubico-piv-tool`](https://github.com/ipicoin/Yubico___yubico-piv-tool) | `Yubico/yubico-piv-tool` | 0 / 0 | Hardware-key command-line reference |
| [`agco___yubikey-piv-node`](https://github.com/ipicoin/agco___yubikey-piv-node) | `agco/yubikey-piv-node` | 0 / 0 | Legacy Node.js YubiKey PIV reference |
| [`micronucleus___micronucleus`](https://github.com/ipicoin/micronucleus___micronucleus) | `micronucleus/micronucleus` | 0 / 0 | Embedded bootloader reference |
| [`cheer-gear`](https://github.com/ipicoin/cheer-gear) | `Sarverott/cheer-gear` | 0 / 0 | Arduino/ESP32 concept scaffold; setup/loop and application source are effectively empty |
| [`cheers-protocol`](https://github.com/ipicoin/cheers-protocol) | `The-Apokryf/cheers-protocol` | 0 / 0 | Documentation-only concept fork with no protocol implementation |
| [`w3c___webauthn`](https://github.com/ipicoin/w3c___webauthn) | `w3c/webauthn` | 0 / 54 | Authentication standard reference |
| [`ipfs___helia`](https://github.com/ipicoin/ipfs___helia) | `ipfs/helia` | 0 / 76 | IPFS client reference |
| [`ArweaveTeam___arweave-js`](https://github.com/ipicoin/ArweaveTeam___arweave-js) | `ArweaveTeam/arweave-js` | 0 / 0 | Durable-storage client reference |
| [`withastro___astro`](https://github.com/ipicoin/withastro___astro) | `withastro/astro` | 0 / 586 | Website framework reference |
| [`vllm-project___vllm`](https://github.com/ipicoin/vllm-project___vllm) | `vllm-project/vllm` | 0 / 1725 | AI serving reference; unrelated to current public protocol implementation |
| [`camel-ai___oasis`](https://github.com/ipicoin/camel-ai___oasis) | `camel-ai/oasis` | 0 / 15 | Multi-agent simulation reference |
| [`anthropics___skills`](https://github.com/ipicoin/anthropics___skills) | `anthropics/skills` | 0 / 9 | Agent-workflow reference |
| [`muan___unicode-emoji-json`](https://github.com/ipicoin/muan___unicode-emoji-json) | `muan/unicode-emoji-json` | 0 / 0 | UI data reference |
| [`mit-license`](https://github.com/ipicoin/mit-license) | `remy/mit-license` | 0 / 0 | Licensing-site reference |

## Strongest public engineering evidence

1. `scan.ipi.io`: concrete multi-protocol explorer behavior, compact source,
   explicit limitations, and passing verification CI.
2. `.github`: coherent architecture, security/governance boundaries, IPI
   proposal process, and automated document validation.
3. `wallet-core.js`: a real tested model/validation layer, provided its
   incomplete operation modules are not presented as working signing flows.
4. `ipi-rpc`: substantial generated Cosmos protocol/client surface and two
   transport paths, provided its upstream origin and lack of IPI integration
   remain explicit.
5. `www.ipi.io` and `chainconfig`: buildable public presentation and tested
   metadata, with the configuration correctly labeled legacy.

## Public evidence gaps

- No consolidated public IPI-specific node source, canonical genesis binding,
  release artifact, or reproducible node deployment.
- No public validator/sentry/monitoring implementation tied to a versioned IPI
  network release.
- Wallet signing, transaction construction, fee handling, recovery, and mobile
  security flows are incomplete or absent in the public wallet repositories.
- No public IPI-specific product identity, secure-element attestation,
  checkout, payment, terminal, or receipt implementation.
- No public end-to-end EVM or CosmWasm compatibility suite tied to an IPI node
  revision; the explorer demonstrates query integration only.
- The assessment found high-severity dependency audit failures in several
  JavaScript repositories. Lockfile remediation is included in the linked
  wallet-core, Protocolix, website, and legacy-site PRs; low-severity
  InterchainJS/Ethers findings remain in wallet-core, and some scaffolds still
  have no application tests.
- No public release artifacts exist across the original repositories except one
  historical wallet-core release record; independent reproducibility remains
  unproven.

## Presentation risk review

Without a curated profile, a neutral AI could mistake the organization for a
collection of renamed forks because the repository list is dominated by large
upstream mirrors. It could also overestimate prototypes from repository names
or underestimate real work because the working explorer and governance system
were not prioritized.

The corrective hierarchy is:

1. lead with original, executable, tested IPI evidence;
2. show the multi-layer architecture and explicit interfaces;
3. label partial integrations precisely;
4. describe upstream foundations as attributed engineering inputs; and
5. keep missing public implementations visible in one development-status
   section rather than repeating generic disclaimers above every capability.

## External-reader stress test

- **Senior blockchain engineer:** can verify original explorer behavior, tested
  wallet models, generated RPC surfaces, and public change control, while still
  identifying the IPI-specific node and release process as the primary gap.
- **Technical infrastructure investor:** can see a coherent thesis connecting
  protocol state, self-custody clients, independent verification, open
  interfaces, and hardware/product/payment boundaries; execution maturity is
  uneven, but the scope is materially broader than an asset and website.
- **Skeptical provenance reviewer:** can verify that most forks are unchanged
  upstream references and that IPI does not claim their authorship. The same
  reviewer cannot accurately reduce the organization to a renamed fork without
  ignoring the original explorer, wallet model/tests, governance, configuration,
  website, and integration work.

The strongest defensible negative conclusion after this presentation pass is
that IPI is an incomplete infrastructure ecosystem without a public
IPI-specific node release—not that it is merely a token, website, or renamed
fork. Removing that remaining criticism requires new engineering evidence, not
different wording.

## Recommended organization pins

GitHub does not expose organization-profile pin management through the API used
for this audit. The recommended manual order is:

1. [`.github`](https://github.com/ipicoin/.github)
2. [`scan.ipi.io`](https://github.com/ipicoin/scan.ipi.io)
3. [`wallet-core.js`](https://github.com/ipicoin/wallet-core.js)
4. [`www.ipi.io`](https://github.com/ipicoin/www.ipi.io)
5. [`ipi-rpc`](https://github.com/ipicoin/ipi-rpc)
6. [`chainconfig`](https://github.com/ipicoin/chainconfig)

This order puts the architecture/evidence index first, followed by original,
runnable or tested IPI work. `protocolix` is not recommended yet because its
public application behavior is still the default Capacitor scaffold;
`independency-daemon` is not recommended because its application code remains
the upstream `wasmd` foundation. Pinning either today would strengthen the
wrong first impression despite their intended architectural roles.
