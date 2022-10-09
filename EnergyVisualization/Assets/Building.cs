using UnityEngine;

public class Building : MonoBehaviour, IBuilding
{
    [SerializeField] private string _name;

    private Transform building;
    private Material material;
    private MeshRenderer meshRenderer;
    private Outline outline;

    private Vector3 nameTagOffset;

    public string Name => _name;
    public Vector3 Position => building.position + nameTagOffset;

    private void Awake()
    {
        building = transform;
        meshRenderer = GetComponent<MeshRenderer>();
        outline = GetComponent<Outline>();
        material = meshRenderer.material;
    }

    private void Start()
    {
        Adjust();
    }

    public void Adjust()
    {
        DataManager dm = DataManager.Instance;
        BuildingManager bm = BuildingManager.Instance;

        float data = dm.GetData(_name);
        float height = bm.MaxBuildingHeight * dm.GetRatio(data);

        material.color = dm.GetColorFromData(data);
        building.localScale = new Vector3(building.localScale.x, height, building.localScale.z);
        building.position = new Vector3(building.position.x, height / 2, building.position.z);
        nameTagOffset = Vector3.right * building.localScale.x;

        // Hide buildings with data 0 or they will produce visual artifacts
        meshRenderer.enabled = !Mathf.Approximately(0, data);
    }

    public void Select()
    {
        outline.enabled = true;
    }

    public void Deselect()
    {
        outline.enabled = false;
    }
}
